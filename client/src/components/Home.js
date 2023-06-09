import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';

function Home() {

    const [index, setIndex] = useState(0);
    const [posts, setPosts] = useState([]);

    const history = useHistory();

    const numPosts = posts.length;
    let maxIndex = numPosts - (numPosts % 5)
    if (numPosts % 5 === 0) maxIndex = maxIndex - 5;

    const handleClickForward = () => {
        if (index < maxIndex) {
            setIndex(index + 5);
        }
    };

    const handleClickBack = () => {
        if (index > 0) {
            setIndex(index - 5);
        }
    };

    const handleClickPost = (e) => {
        const user_id = e.currentTarget.getAttribute('user_id');
        history.push(`profile/${user_id}`)
    };

    useEffect(() => {
        fetch('/posts')
        .then(res => res.json())
        .then((data) => setPosts(data.reverse()));
    }, []);

    if (!posts) {
        return <h1>Loading</h1>
    } else {
        const postList = posts.slice(index, index+5).map((post, index) => {    
            const { content, user, user_id } = post;
            const { name, photo } = user;
            
            return (
                <ul key={index} className='post-container'>
                    <div className='div-post' user_id={user_id} onClick={handleClickPost}>
                        <div className='post-img-name-container'>
                            <img 
                                src={photo} 
                                className='img-post' 
                                alt={name} 
                            />
                            <span>{name}</span>
                        </div>
                        <p>{content}</p>
                        {/* <span onClick={handleClickLike}>❤ {likes}</span> */}
                    </div>
                </ul>
            );
        });

        return (
            <>
                <div className='scroll-button-container'>
                    <button className='scroll-button' onClick={handleClickBack}>
                        {index === 0 ? '---' : '←'}
                    </button>
                    <button className='scroll-button' onClick={handleClickForward}>
                        {index === maxIndex ? '---' : '→'}
                    </button>
                </div>
                {postList}
                <div className='scroll-button-container'>
                    <button className='scroll-button' onClick={handleClickBack}>
                        {index === 0 ? '---' : '←'}
                    </button>
                    <button className='scroll-button' onClick={handleClickForward}>
                        {index === maxIndex ? '---' : '→'}
                    </button>
                </div>
            </>
        );
    };
}

export default Home;