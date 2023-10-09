import React from "react";

const SearchTypeSelector = ({ defaultValue, setSearchType }) => {
  return (
    <div className="search-type">
      <label for="search-select">Select search type</label>
      <select
        style={{ fontSize: "17px" }}
        id="search-select"
        onChange={(event) => setSearchType(event.target.value)}
        defaultValue={defaultValue}
      >
        <option value="hybrid">Hybrid (vector + text)</option>
        <option value="vector">Vector</option>
        <option value="text">Text</option>
      </select>
    </div>
  );
};

export default SearchTypeSelector;
