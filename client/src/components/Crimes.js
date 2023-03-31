import { useState, useEffect } from 'react';
import { useFormik } from "formik";
import { useHistory } from 'react-router-dom';

function Crimes({user}){

    const history = useHistory();
    const [crimes, setCrimes] = useState([]);
    const [newCrime, setNewCrime] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        fetch('/crimes')
        .then(res => res.json())
        .then((data) => {
            setCrimes(data.reverse())
            setIsLoaded(current => !current);
        });
    }, []);

    function newCrimeButton(){
        setNewCrime(current => !current)
    }

    function editButton(e){
        history.push(`/crimes/${e.target.name}`)
    }

    function deleteButton(e){
        if(window.confirm('Are you sure you want to delete this crime? Click OK to confirm.') === true){
            fetch('/crimes/'+e.target.name, {
                method: "DELETE",
            })
            .then(res => {
                if(res.ok){
                    setCrimes(crimes=> crimes.filter((crime) => parseInt(crime.id)!==parseInt(e.target.name)))
                }
            })
        }
    }

    const formik = useFormik({
        initialValues: {
            name: '',
            description: ''
        },
        onSubmit: (values, {resetForm}) => {
            fetch('/crimes', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) {
                    res.json().then(data => {
                        setCrimes([data, ...crimes]);
                        newCrimeButton();
                        resetForm();
                        history.push('/crimes');
                    })
                } else {
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })

    if (!isLoaded) return <h1>Loading...</h1>;
    if ((user&&user.is_admin === false) || (!user)) {
        return <h1>...</h1>
    } else {
        return (
            <>
                <center><button onClick={newCrimeButton}>Create a new crime</button></center>
                {newCrime?<div className='new-crime-form'>
                    <form onSubmit={formik.handleSubmit} >
                    <label >Name of Crime</label>
                    <input type="text"  name="name" value={formik.values.name} onChange={formik.handleChange} />
                    <br></br>
                    <label >Description</label>
                    <textarea type="text"  name="description" value={formik.values.description} onChange={formik.handleChange} />
                    <br></br>
                    <input type='submit' value='Save' />
                </form>
                </div>:''}
                <center><h2>Edit Available Crimes:</h2></center>
                <div className="crimes">
                    {crimes.map((crime, index) => (
                        <ul key={index} className='singlecrime'>{crime.name}
                            <p>{crime.description}</p>
                            <button onClick={editButton} name={crime.id}>Edit</button>
                            <button onClick={deleteButton} name={crime.id}>Delete</button>
                        </ul>
                    ))}
                </div>
            </>
        )
    }
}

export default Crimes;