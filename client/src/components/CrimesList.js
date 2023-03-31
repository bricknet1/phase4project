import { useState, useEffect } from 'react';
import { useFormik } from "formik";

function CrimesList({user}){

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

    function handleDelete(e){
        if(window.confirm('Are you sure you want to delete this crime? Click OK to confirm.') === true){
            fetch('/usercrimes/'+e.target.id, {
                method: "DELETE",
            })
            .then(res => {
                if(res.ok){
                    setMyCrimes(crimes=> crimes.filter((crime) => parseInt(crime.id)!==parseInt(e.target.id)))
                }
            })
        }
    }

    if(!user||!isLoaded){return(<h3>Loading...</h3>)}
    if(user&&isLoaded){
        return(
            <>
            {/* <h1>My Crimes</h1> */}
            <div className='add-personal-crime'>
                <h2>Add a Crime</h2>
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
            <div className="user-crimes">
                    <h2>My Crimes</h2>
                    <ul>
                        {myCrimes.map((crime, index) => (
                            <li key={index}>{crime.name} - <span className='deletecrime' id={crime.id} onClick={handleDelete}>Delete This Crime</span>
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