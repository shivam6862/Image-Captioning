import React from "react";
import classes from "./HomePage.module.css";
import UploadImage from "../ImageUploder/UploadImage";

const HomePage = () => {
  return (
    <div className={classes.container}>
      <div className={classes.UploadImagepart}>
        <UploadImage />
      </div>
    </div>
  );
};

export default HomePage;
