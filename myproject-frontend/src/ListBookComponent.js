import axios from 'axios';
import React, { useEffect, useState, useCallback } from 'react';
axios.defaults.withCredentials = true;
function ListBookComponent() {
    const [bookList, setBookList] = useState([]);
    const apiURL = "http://127.0.0.1:8000/api/listbooks/";
    const fetchData = useCallback(async () => { // {{ edit_1 }}
        const response = await axios.get(apiURL, { 'withCredentials': true });
        console.log(response);
        setBookList(response.data);
    }, [apiURL]); // {{ edit_2 }}
    useEffect(() => {
        fetchData(); // Call the fetchData function
    }, [fetchData]); // {{ edit_3 }}
    return (
        <div className="main-section">
            <h1>All Books</h1>
            <div className="book-list">
                {bookList.map((book, index) => (
                    <ul>
                        <li>Book: {book.name}</li>
                        <li>Author: {book.author}</li>
                    </ul>
                ))}
            </div>
        </div>
    );
}
export default ListBookComponent;
