import React, { useState } from "react";
import "./HomePage.css";
import LoadingIcon from "./LoadingIcon";
import SearchTypeSelector from "./components/SearchTypeSelector";
import { BiLinkExternal } from 'react-icons/bi';

const HomePage = () => {
  const [news, setNews] = useState();
  const [searchType, setSearchType] = useState("hybrid");
  const [loading, setLoading] = useState(false);

  const handleSearch = async (event) => {
    event.preventDefault();
    const searchTerm = event.target.querySelector(".search-input").value;
    setLoading(true);

    try {
      await fetch("/api/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          searchInput: searchTerm,
          searchType: searchType,
        }),
      })
        .then((res) => res.json())
        .then((d) => {
          const dataJson = JSON.parse(d);
          setNews(dataJson.data.Get.Article);
        });
      setLoading(false);
    } catch (error) {
      console.log("Something went wrong with the API call.");
      setLoading(false);
    }
  };

  return (
    <div className="home-page">
      <div className="header">
        <span className="header-text">REALLY GOOD NEWS ONLY TODAY</span>
      </div>
      <form onSubmit={handleSearch} className="search-bar">
        <input
          required
          type="text"
          className="search-input"
          placeholder="Search with any text..."
        />
        <SearchTypeSelector
          defaultValue={searchType}
          setSearchType={setSearchType}
        />
        <input type="submit" className="search-button" value="Search" />
      </form>
      <div className="results-container">
        {news.map((article) => (
          <div className="news-article" key={article.id}>
            <div className="title-row">
              <h2 className="news-title">
                <a href={article.url} target="_blank" rel="noopener noreferrer">
                  {article.title}
                </a>
                <BiLinkExternal style={{marginLeft: '2px'}} />
              </h2>
              <div className="relevancy-score">
                <span style={{ textDecoration: "underline" }}>
                  Relevancy score
                </span>
                <span className="pill">0.12312512312</span>
              </div>
            </div>
            <div className="article-details">
              <span>Author: {article.author}</span>
              <span>Published: {article.date}</span>
            </div>
            <div className="article-content">
              <p>{article.text}</p>
            </div>
          </div>
        ))}
        {loading && <LoadingIcon />}
      </div>
    </div>
  );
};

export default HomePage;
