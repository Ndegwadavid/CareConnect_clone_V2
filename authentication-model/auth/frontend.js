fetch("http://localhost:3000/secret-keys", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ key: keyValue }),
})
  .then((response) => {
    // Handle the response
  })
  .catch((error) => {
   //handle any erros to be received
  });
