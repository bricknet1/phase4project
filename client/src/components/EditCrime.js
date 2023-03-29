import {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import { useFormik } from "formik";
import { useHistory } from 'react-router-dom';

function EditCrime({user}) {

    const history = useHistory();
    
    const {id} = useParams();

    const [crime, setCrime] = useState({
        "name":'',
        "description":''
    });
    const [isLoaded, setIsLoaded] = useState(false);

    const formik = useFormik({
        enableReinitialize: true,
        initialValues: {
            name: crime.name,
            description: crime.description
        },
        onSubmit: (values) => {
            fetch(`/crimes/${id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) {
                    res.json().then(data => {
                        setCrime(data)
                        history.push('/crimes')
                    })
                } else {
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })

    useEffect(()=>{
        fetch('/crimes/'+id)
        .then(res=>res.json())
        .then((data) => {
            setCrime(data);
            setIsLoaded(current => !current);
        })
    }, [id])

    if (!isLoaded) return <h1>Loading...</h1>;
    if ((user&&user.is_admin === false) || (!user)) {
        return <h1>...</h1>
    } else {
        return (
            <>
                <div className='new-crime-form'>
                    <form onSubmit={formik.handleSubmit} >
                        <label >Name of Crime</label>
                        <input type="text"  name="name" value={formik.values.name} onChange={formik.handleChange} />
                        <br></br>
                        <label >Description</label>
                        <input type="text"  name="description" value={formik.values.description} onChange={formik.handleChange} />
                        <br></br>
                        <input type='submit' value='Save' />
                    </form>
                </div>
            </>
        );
    }
}


export default EditCrime;