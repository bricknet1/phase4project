import { useState, useEffect } from 'react';

function Crimes({user}){

    const [crimes, setCrimes] = useState([]);

    useEffect(() => {
        fetch('/crimes')
        .then(res => res.json())
        .then((data) => setCrimes(data));
    }, []);

    function editButton(){
        console.log('edit');
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

    if (user&&user.is_admin === false){
        return <h1>NOT AUTHOIRIZED</h1>
    } else {
        return (
            <>
                <button>Create a new crime</button>
                <h2>Edit Available Crimes:</h2>
                <div className="crimes">
                    <ul>
                        {crimes.map((crime, index) => (
                            <li key={index} className='singlecrime'>{crime.name}
                                <button onClick={editButton}>Edit</button>
                                <button onClick={deleteButton} name={crime.id}>Delete</button>
                                <ul>
                                    <li>Lethal: {crime.lethal?"Yes":"No"}</li>
                                    <li>Misdemeanor: {crime.misdemeanor?"Yes":"No"}</li>
                                    <li>Felony: {crime.felony?"Yes":"No"}</li>
                                    <li>Description: {crime.description}</li>
                                    <br></br>
                                </ul>
                            </li>
                        ))}
                    </ul>
                </div>
            </>
        )
    }

}

export default Crimes;