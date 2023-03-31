import { useFormik } from "formik";
import { useHistory } from 'react-router-dom';

function NewPost({user}) {

    const history = useHistory();

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
                    res.json().then(history.push('/'))
                } else {
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })

    if (!user) {
        return <h1>Not Authorized</h1>
    } else {
    return(
        <div className='new-post'>
            <h1>New Post</h1>
            <form onSubmit={formik.handleSubmit}>
                <div className="new-post-container">
                    <textarea type="text"  name="content" value={formik.values.content} onChange={formik.handleChange} />
                </div>
                <input type='submit' value='Submit' />
            </form>
        </div>
    )}
}

export default NewPost;