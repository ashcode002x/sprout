from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit, join_room, leave_room
import uuid
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY","alskfnj#)F@*($Cfdivnrfc[qi") 
socketio = SocketIO(app, cors_allowed_origins=os.environ.get("SOCKET_CORS_ALLOWED_ORIGINS", "*"))

# Store active users and their room assignments
active_users = {}
room_participants = {}

@app.route('/')
def index():
    """Render the main meeting interface"""
    return render_template('index.html')

@app.route('/join/<meeting_id>')
def join_meeting(meeting_id):
    """Join a specific meeting room"""
    return render_template('meeting.html', meeting_id=meeting_id)

@socketio.on('connect')
def handle_connect():
    """Handle new connection"""
    user_id = str(uuid.uuid4())
    session['user_id'] = user_id
    active_users[user_id] = {'username': request.sid, 'room': None}
    emit('connected', {'user_id': user_id})
    print(f'Client connected: {user_id}')

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnect"""
    user_id = session.get('user_id')
    if user_id in active_users:
        room = active_users[user_id]['room']
        if room and room in room_participants and user_id in room_participants[room]:
            room_participants[room].remove(user_id)
            emit('user_left', {'user_id': user_id}, room=room)
        del active_users[user_id]
    print(f'Client disconnected: {user_id}')

@socketio.on('join_room')
def handle_join_room(data):
    """Handle user joining a meeting room"""
    user_id = session.get('user_id')
    room = data['room']
    
    if user_id in active_users:
        join_room(room)
        active_users[user_id]['room'] = room
        
        # Initialize room if it doesn't exist
        if room not in room_participants:
            room_participants[room] = []
        
        room_participants[room].append(user_id)
        
        # Notify others in the room
        emit('user_joined', {
            'user_id': user_id,
            'username': data.get('username', f'User-{user_id[:8]}')
        }, room=room)
        
        # Send list of existing users to the new participant
        emit('room_participants', {
            'participants': [{'user_id': uid, 'username': active_users[uid].get('username')} 
                           for uid in room_participants[room] if uid != user_id]
        })

# Screen sharing
@socketio.on('screen_share_start')
def handle_screen_share(data):
    """Handle screen sharing start"""
    user_id = session.get('user_id')
    room = active_users[user_id]['room']
    emit('screen_share_started', {
        'user_id': user_id,
        'stream_id': data['stream_id']
    }, room=room)

@socketio.on('screen_share_stop')
def handle_screen_share_stop():
    """Handle screen sharing stop"""
    user_id = session.get('user_id')
    room = active_users[user_id]['room']
    emit('screen_share_stopped', {'user_id': user_id}, room=room)

# Video streaming
@socketio.on('video_offer')
def handle_video_offer(data):
    """Handle WebRTC video offer"""
    target_id = data['target']
    emit('video_offer', {
        'sdp': data['sdp'],
        'user_id': session.get('user_id')
    }, room=request.sid)

@socketio.on('video_answer')
def handle_video_answer(data):
    """Handle WebRTC video answer"""
    target_id = data['target']
    emit('video_answer', {
        'sdp': data['sdp'],
        'user_id': session.get('user_id')
    }, room=request.sid)

@socketio.on('new_ice_candidate')
def handle_new_ice_candidate(data):
    """Handle WebRTC ICE candidate"""
    target_id = data['target']
    emit('new_ice_candidate', {
        'candidate': data['candidate'],
        'user_id': session.get('user_id')
    }, room=request.sid)

# Audio control
@socketio.on('audio_toggle')
def handle_audio_toggle(data):
    """Handle user audio toggle"""
    user_id = session.get('user_id')
    room = active_users[user_id]['room']
    emit('user_audio_toggle', {
        'user_id': user_id,
        'enabled': data['enabled']
    }, room=room)

# Video control
@socketio.on('video_toggle')
def handle_video_toggle(data):
    """Handle user video toggle"""
    user_id = session.get('user_id')
    room = active_users[user_id]['room']
    emit('user_video_toggle', {
        'user_id': user_id,
        'enabled': data['enabled']
    }, room=room)

# Chat functionality
@socketio.on('chat_message')
def handle_chat_message(data):
    """Handle chat messages"""
    user_id = session.get('user_id')
    room = active_users[user_id]['room']
    username = data.get('username', f'User-{user_id[:8]}')
    
    emit('new_chat_message', {
        'user_id': user_id,
        'username': username,
        'message': data['message'],
        'timestamp': data.get('timestamp', None)
    }, room=room)

# Raise hand functionality
@socketio.on('raise_hand')
def handle_raise_hand():
    """Handle raise hand notification"""
    user_id = session.get('user_id')
    room = active_users[user_id]['room']
    username = active_users[user_id].get('username', f'User-{user_id[:8]}')
    
    emit('user_raised_hand', {
        'user_id': user_id,
        'username': username
    }, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=os.environ.get("FLASK_DEBUG", "True")=="True")