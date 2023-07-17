import React, { useState } from "react";
import SvgSave from "../ui/SvgSave";
import classes from "./UploadImage.module.css";

const UploadImage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [setImageToBackend, setsetImageToBackend] = useState();
  const [text, setText] = useState("IMAGE TEXT");

  const handleFileUpload = (event) => {
    const file = event.target.files?.[0];
    const reader = new FileReader();
    setsetImageToBackend(file);
    if (file) {
      reader.onload = (e) => {
        setSelectedImage(e.target?.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const saveImage = async () => {
    if (selectedImage == null) return;
    console.log(setImageToBackend);
    const formData = new FormData();
    if (setImageToBackend) {
      formData.append("file", setImageToBackend);
    }
    try {
      const response = await fetch(
        `${import.meta.env.VITE_REACT_BACKEND_URL}/image/`,
        {
          method: "POST",
          body: formData,
        }
      );
      const responsedata = await response.json();
      console.log(responsedata);
      setText(responsedata.message);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className={classes.container}>
      <div className={classes.file_input_wrapper}>
        <input
          type="file"
          id="userimage"
          name="userimage"
          className={classes.file_input}
          onChange={handleFileUpload}
        />
        <div className={classes.part1_b_a}>
          {selectedImage && <img src={selectedImage} alt="Uploaded Image" />}
        </div>
        <label htmlFor="userimage" className={classes.file_input_label}>
          Choose a file
        </label>
        <div
          className={classes.svgsave}
          onClick={() => {
            saveImage();
          }}
        >
          <SvgSave />
        </div>
      </div>
      <div className={classes.text}>{text}</div>
    </div>
  );
};

export default UploadImage;
