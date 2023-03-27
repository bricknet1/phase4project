import {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';

function Profile({user}) {
    
    const {id} = useParams();

    const [profile, setProfile] = useState(null);

    useEffect(()=>{
        fetch('/users/'+id)
        .then(res=>res.json())
        .then((data) => {
            setProfile(data)
        })
    }, [id])
    
    
    if(!profile){
        return <h1>loading</h1>
    } else {
        
        const {name, bio, photo, email, is_admin, crimes} = profile
        
        return (
            <>
            <h1>{name}</h1>
            <p>{bio}</p>
            <img src={photo} />
            <p>{email}</p>
            </>
        );
    }
}

export default Profile;