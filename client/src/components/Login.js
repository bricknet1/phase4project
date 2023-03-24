import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { useFormik } from "formik";
import * as yup from "yup";

function Login({ setUser }) {

    const history = useHistory();
    const [error, setError] = useState();

    const formSchema = yup.object().shape({
        email: yup.string().email()
    });

    const formik = useFormik({
        initialValues: {
            email: '',
            password: ''
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) {
                    res.json().then(user => {
                        console.log(user)
                        setUser(user)
                        history.push('/home')
                    })
                } else {
                    console.log('nope')
                    res.json().then(error => setError(error.message))
                };
            })
        }
    })

    return (
        <>
            <h1>Login</h1>
            <h2 style={{color:'red'}}> {formik.errors.email}</h2>
            {error&& <h2 style={{color:'red'}}> {error}</h2>}
            
            <form onSubmit={formik.handleSubmit}>
                <label >Email</label>
                <input type="text"  name="email" value={formik.values.email} onChange={formik.handleChange} />
                <label >Password</label>
                <input type="text"  name="password" value={formik.values.password} onChange={formik.handleChange} />
                <input type='submit' value={'Log In!'} />
            </form>
        </>
    );
}

export default Login;