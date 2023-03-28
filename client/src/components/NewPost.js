import { useFormik } from "formik";
import { useHistory } from 'react-router-dom';
import { useState } from 'react';

function NewPost({user}) {

    console.log(user);

    const history = useHistory();
    const [error, setError] = useState('');

    const formik = useFormik({
        enableReinitialize: true,
        initialValues: {
            content: '',
            likes: 0
        },
        onSubmit: (values) => {
            fetch('/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) {
                    res.json().then(data => {
                        console.log(data)
                        history.push('/home')
                    })
                } else {
                    console.log('nope')
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })

    return(
        <div className='new-post'>
            <form onSubmit={formik.handleSubmit}>
                <label >New Post:</label>
                <input type="text"  name="content" value={formik.values.content} onChange={formik.handleChange} />
                <input type='submit' value='Submit' />
            </form>
        </div>
    )
}

export default NewPost;