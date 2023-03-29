import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { useFormik } from "formik";
import * as yup from "yup";

function Login({ setUser }) {

    const history = useHistory();
    const [error, setError] = useState('');
    const [signup, setSignup] = useState(false);

    const handleClick = () => setSignup(!signup)

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
            fetch(signup?'/signup':'/login', {
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
                        if (signup){history.push('/profile/'+user.id)}
                        else {history.push('/')}
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
            <h1>{signup?'Create An Account':'Login'}</h1>
            <h2 style={{color:'red'}}> {formik.errors.email}</h2>
            {error&& <h2 style={{color:'red'}}> {error}</h2>}
            <button onClick={handleClick}>{signup?'Already have an account? Log in':'New here? Sign up'}</button>
            <form onSubmit={formik.handleSubmit}>
                <label >Email</label>
                <input type="text"  name="email" value={formik.values.email} onChange={formik.handleChange} />
                <label >Password</label>
                <input type="text"  name="password" value={formik.values.password} onChange={formik.handleChange} />
                <input type='submit' value={signup?'Create Account!':'Log In!'} />
            </form>

        </>
    );
}

export default Login;