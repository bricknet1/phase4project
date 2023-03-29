import {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import { useFormik } from "formik";
import * as yup from "yup";
import { useHistory } from 'react-router-dom';

function Profile({user}) {
    
    console.log(user);

    const history = useHistory();
    
    const {id} = useParams();

    const thisuser = user?user.id==id:false
    console.log(thisuser);

    const [profile, setProfile] = useState({
        "name":'',
        "description":'',
        "date":'',
        "caught":'',
        "convicted":''
    });
    const [editMode, setEditMode] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    // const [error, setError] = useState('');
    
    function handleClick(){
        setEditMode(current=>!current)
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
            handleClick();
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
                        console.log(data)
                        setProfile(data)
                        history.push('/profile/'+id)
                    })
                } else {
                    console.log('nope')
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })



    useEffect(()=>{
        fetch('/users/'+id)
        .then(res=>res.json())
        .then((data) => {
            setProfile(data);
            setIsLoaded(current => !current);
        })
    }, [id])


    if (!isLoaded) return <h1>Loading...</h1>;


    const {name, bio, photo, email, is_admin, crime_list} = profile

    return (
        <>
            <h1>{name}</h1>
            <p>{bio}</p>
            <img src={photo} />
            <p>{email}</p>
            <p>Admin: {is_admin?'Yes':'No'}</p>
            {thisuser?<button onClick={handleClick}>{editMode?'Close Editor Without Saving':'Edit Profile'}</button>:''}
            {editMode?<div className='profile-edit'>
                <form onSubmit={formik.handleSubmit} enableReinitialize>
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
            <div className="crimes">
                <h3>Crimes:</h3>
                <ul>
                    {crime_list.map((crime, index) => (
                        <li key={index}>{crime.name}
                            <ul>
                                <li>Date committed: {crime.date}</li>
                                <li>Caught: {crime.caught?"Yes":"No!"}</li>
                                <li>Convicted: {crime.convicted?"Yes":"No!"}</li>
                            </ul>
                        </li>
                    ))}
                </ul>
            </div>
        </>
    );
}


export default Profile;