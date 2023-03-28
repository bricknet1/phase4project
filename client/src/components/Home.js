import { useState, useEffect } from 'react';

function Home() {

    const [index, setIndex] = useState(0);
    const [posts, setPosts] = useState([]);

    const numPosts = posts.length;
    let maxIndex = numPosts - (numPosts % 5)
    if (numPosts % 5 == 0) maxIndex = maxIndex - 5;

    console.log(numPosts)
    console.log(maxIndex)

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

    useEffect(() => {
        fetch('/posts')
          .then(res => res.json())
          .then((data) => setPosts(data.reverse()));
    }, []);

    if (!posts) {
        return <h1>Loading</h1>
    } else {
        const postList = posts.slice(index, index+5).map((post, index) => {    
            const { content, likes, user } = post;
            const { name, photo } = user;
            
            return (
                <ul key={index}>
                    <div className='div-post'>
                        <div>
                            <img src={photo} className="img-post" alt={name} />
                            <span>{name}</span>
                        </div>
                        <p>{content}</p>
                        <span>❤ {likes}</span>
                    </div>
                </ul>
            );
        });

        return (
            <>
                <button onClick={handleClickBack}>
                    {index === 0 ? '---' : '←'}
                </button>
                <button onClick={handleClickForward}>
                    {index === maxIndex ? '---' : '→'}
                </button>
                <ul>{postList}</ul>
                <button onClick={handleClickBack}>
                    {index === 0 ? '---' : '←'}
                </button>
                <button onClick={handleClickForward}>
                    {index === maxIndex ? '---' : '→'}
                </button>
            </>
        );
    };
}

export default Home;