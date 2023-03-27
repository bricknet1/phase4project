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
        
        const {name, bio, photo, email, is_admin, crime_list} = profile

        // debugger;

        return (
            <>
            <h1>{name}</h1>
            <p>{bio}</p>
            <img src={photo} />
            <p>{email}</p>
            <div className="crimes">
                <h3>Crimes:</h3>
                <ul>
                    {crime_list.map((crime, index) => (
                        <li key={index}>{crime.name}
                            <ul>
                                <li>Date committed: {crime.date}</li>
                                <li>Caught: {crime.caught?"True":"False"}</li>
                                <li>Convicted: {crime.convicted?"True":"False"}</li>
                            </ul>
                        </li>
                    ))}
                </ul>
            </div>
            </>
        );
    }
}

export default Profile;