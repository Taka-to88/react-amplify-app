import axios from "axios";
import React, { useEffect, useState } from "react";

const ApiFetch = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios
      .get("https://test-api-gateway-30i53yrj.an.gateway.dev/get-time")
      .then((res) => {
        setPosts(res.data);
      });
  }, []);

  return (
    <div>
      <a> {posts.message} </a>
    </div>
  );
};

export default ApiFetch;
