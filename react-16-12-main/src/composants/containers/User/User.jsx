import React from "react";
import Fullname from "./Fullname";
import Hobbies from "./Hobbies";

const User = () => {
  return (
    <div>
      <h2>Profil Utilisateur</h2>
      <h3>Nom Complet :</h3>
      <Fullname />
      <h3>Passions :</h3>
      <Hobbies />
    </div>
  );
};

export default User;
