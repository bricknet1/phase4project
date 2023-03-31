import {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import { useFormik } from "formik";
import * as yup from "yup";
import { useHistory } from 'react-router-dom';

function Profile({user}) {

    const [editMode, setEditMode] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    const [messages, setMessages] = useState([]);
    const [newMessage, setNewMessage] = useState('');

    const history = useHistory();

    const {id} = useParams();

    const thisUser = user?user.id===parseInt(id):false
    
    const [profile, setProfile] = useState({
        "name":'',
        "description":'',
        "date":'',
        "caught":'',
        "convicted":''
    });

    let isAFriend = false;
    if (user) {
        const friendIds = user.friends.map(friend => friend.id);
        isAFriend = thisUser ? false : friendIds.includes(parseInt(id));
    }
    
    function handleClickEdit(){
        setEditMode(current=>!current)
    }
    
    function handleClickAddFriend() {
        fetch('/friendships', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: parseInt(id),
                friend_id: parseInt(user.id)
            })
        })
        .then(res => {
            if (res.ok) {
                isAFriend = true;
                window.location.reload(true);
            } else console.log('error adding friend');
        })
    }
    
    function handleClickRemoveFriend() {
        fetch('/friendships', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: parseInt(user.id),
                friend_id: parseInt(id)
            })
        })
        .catch(err => console.log(err))
        window.location.reload(true);
    }

    const formSchema = yup.object().shape({
        email: yup.string().email()
    });

    const formik = useFormik({
        enableReinitialize: true,
        initialValues: {
            name: profile.name,
            bio: profile.bio,
            photo: profile.photo,
            email: profile.email
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            handleClickEdit();
            fetch(`/users/${id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) {
                    res.json().then(data => {
                        setProfile(data)
                        history.push('/profile/'+id)
                    })
                } else {
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })

    useEffect(()=>{
        setIsLoaded(false)
        setEditMode(false)
        fetch('/users/'+id)
        .then(res=>res.json())
        .then((data) => {
            setProfile(data);
            setIsLoaded(current => !current);
        })
    }, [id])

    useEffect(() => {
        if(user){
            setMessages([])
            fetch('/messages/'+user.id)
            .then(res => res.json())
            .then((data) => data.forEach(message => {
                if ((message.sender_id === parseInt(id)) || (message.receiver_id === parseInt(id))){setMessages(messages => [...messages, message])}
        }))
        }
    }, [user, id]);

    const messageRender = messages.map((message, index) => {
        return(
            <div key={index}
            className={
                message.sender_id === user.id ? 'sent-message' : 'received-message'
            }>
                <p>
                    {(message.sender_id === user.id) ? "" : profile.name+": "}{message.content}
                </p>
            </div>
        )
    })

    function handleNewMessage(e){
        setNewMessage(e.target.value)
    }
    
    function handleSubmitNewMessage(e){
        e.preventDefault();
        const values = {
            content: newMessage,
            sender_id: user.id,
            receiver_id: id
        }
        fetch('/messages', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
        })
        .then(res => {
            if (res.ok) {
                res.json().then(data => {
                    setMessages([...messages, data]);
                    setNewMessage('');
                })
            } else {
                res.json().then(error => console.log(error.message))
            };
        })
    }
    
    const {name, bio, photo, crime_list, friends} = profile

    if (!isLoaded) return <h1>Loading...</h1>;

    return (
        <div className='profile-container'>
            {/* friends (left) */}
            <div className="profile-friends-container">
                <h3>Friends:</h3>
                <ul className='friend-list-container'>
                    {friends.map((friend, index) => {
                        return (
                            <li key={index}>
                                <div 
                                    className="friend-container"
                                    onClick={() => history.push('/profile/'+friend.id)}
                                >
                                    <img 
                                        className="img-friend-list"
                                        src={friend.photo}
                                        alt={friend.name}
                                    />
                                    <span>{friend.name}</span>
                                </div>
                            </li>
                        );
                    })}
                </ul>
            </div> 
            {/* middle */}
            <div className='profile-middle-container'>
                {/* profile info */}
                <div className='profile-info-container'>
                    <img src={photo} alt={name} className="profile-photo" />
                    <h1>{name}</h1>
                    <p>{bio}</p>
                    {thisUser||!user ? null : 
                        isAFriend ? 
                            <button onClick={handleClickRemoveFriend}>Remove Friend</button> 
                        : 
                            <button onClick={handleClickAddFriend}>Add Friend</button>
                    }
                    {thisUser?<button onClick={handleClickEdit}>{editMode?'Close Editor Without Saving':'Edit Profile'}</button>:''}
                    {editMode?<div className='profile-edit'>
                        <form onSubmit={formik.handleSubmit}>
                            <label >Name</label>
                            <input type="text"  name="name" value={formik.values.name} onChange={formik.handleChange} />
                            <label >Email</label>
                            <input type="text"  name="email" value={formik.values.email} onChange={formik.handleChange} />
                            <label >Bio</label>
                            <input type="text"  name="bio" value={formik.values.bio} onChange={formik.handleChange} />
                            <label >Photo</label>
                            <input type="text"  name="photo" value={formik.values.photo} onChange={formik.handleChange} />
                            <input type='submit' value='Save' />
                        </form>
                    </div>:''}
                </div>
                {/* messages */}
                <div className='profile-messages-container'>
                    {user&&!thisUser?<div>
                        <h3>Messages with this criminal:</h3>
                        <div className='messages-container'>
                            {messageRender}
                        </div>
                        <form onSubmit={handleSubmitNewMessage}>
                            <label >Send this criminal a new message: </label>
                            <input type="text"  name="content" value={newMessage} onChange={handleNewMessage} />
                            <input type='submit' value='Send' />
                        </form>
                    </div>:null}
                </div>
            </div>
            {/* crimes (right) */}
            <div className="profile-crimes-container">
                <h3>Crimes:</h3>
                    {crime_list.map((crime, index) => (
                        <ul key={index} className='crime-list-item'>
                            <u><b>{crime.name}</b></u>
                            <li>Date committed: {crime.date}</li>
                            <li>Caught: {crime.caught?"Yes":"No!"}</li>
                            <li>Convicted: {crime.convicted?"Yes":"No!"}</li>
                        </ul>
                    ))}
                <br></br>
                {thisUser?<a href='/crimeslist'>Add More Crimes</a>:null}
            </div>
        </div>
    );
}


export default Profile;