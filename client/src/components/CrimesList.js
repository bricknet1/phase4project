import { useState, useEffect } from 'react';
import { useFormik } from "formik";
import { useHistory } from 'react-router-dom';

function CrimesList({user}){

    const [profile, setProfile] = useState({});
    const [isLoaded, setIsLoaded] = useState(false);
    const [crimes, setCrimes] = useState([]);
    const [myCrimes, setMyCrimes] = useState([]);

    useEffect(() => {
        fetch('/crimes')
        .then(res => res.json())
        .then((data) => {
            setCrimes(data)
        });
    }, []);

    useEffect(()=>{
        setIsLoaded(false)
        if(user){
            fetch('/users/'+user.id)
            .then(res=>res.json())
            .then((data) => {
                setProfile(data);
                setIsLoaded(current => !current);
                setMyCrimes(data.crime_list.sort((x, y) => (x.data < y.date) ? 1 : (x.date > y.date) ? -1 : 0))
            })
        }
    }, [user])

    const formik = useFormik({
        enableReinitialize: true,
        initialValues: {
            user_id: '',
            crime_id: '',
            date: '',
            caught: false,
            convicted: false
        },
        onSubmit: (values) => {
            values['user_id'] = user.id
            fetch('/usercrimes', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) {
                    res.json().then(data => {
                        let newcrime = data
                        newcrime['name'] = data.crime.name
                        setMyCrimes(myCrimes => [newcrime, ...myCrimes])
                    })
                } else {
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })

    if(!user||!isLoaded){return(<h3>Loading...</h3>)}
    if(user&&isLoaded){
        return(
            <>
            <h1>My Crimes</h1>
            <div className='add-personal-crime'>
                <form onSubmit={formik.handleSubmit} >
                    <label for='crime_id'>Crime: </label>
                    <select id='crime_id' name="crime_id" value={formik.values.crime_id} onChange={formik.handleChange} >
                        <option value='' defaultValue disabled hidden>Select a Crime</option>
                        {crimes.map((crime, index) => (
                            <option key={index} value={crime.id}>{crime.name}</option>))}
                    </select>
                    <br></br>
                    <label >Date Committed: </label>
                    <input type="date"  name="date" value={formik.values.date} onChange={formik.handleChange} />
                    <br></br>
                    <label >Were you caught? </label>
                    <input type="checkbox"  name="caught" checked={formik.values.caught} onChange={formik.handleChange} />
                    <br></br>
                    <label >Were you convicted? </label>
                    <input type="checkbox"  name="convicted" checked={formik.values.convicted} onChange={formik.handleChange} />
                    <br></br>
                    <input type='submit' value='Save' />
                </form>
            </div>
            <div className="crimes">
                    <h3>Crimes:</h3>
                    <ul>
                        {myCrimes.map((crime, index) => (
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
        )
    }
}

export default CrimesList