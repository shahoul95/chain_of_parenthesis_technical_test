import React from "react";

const Hobbies = () => {
  const hobbies = ["Lecture", "Voyage", "Musique"];

  return (
    <ul>
      {hobbies.map((hobby, index) => (
        <li key={index}>{hobby}</li>
      ))}
    </ul>
  );
};

export default Hobbies;
