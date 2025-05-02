document.getElementById("form").addEventListener('submit', 
    async (e) => {
        e.preventDefault();

        const name = document.getElementById("name").value;
        const description = document.getElementById("description").value;
        const price = document.getElementById("price").value;
        // const item_id = document.getElementById("item_id").value;
        
        try{
            const response = await fetch(`http://localhost:8000/create_item`,
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({name,description,price})
                    }
                );


                if (!response.ok) {  // Check if the response status is not OK (i.e., 404 or other errors)
                    const errorData = await response.json();  // Get the error details
                    throw new Error(errorData.detail || "An error occurred");  // Throw an error with the message
                }

                const data = await response.json();
                console.log(data);
                document.getElementById("form").reset();
                alert("Item added successfully!");

            }catch (error){
                console.error("Error:", error.message);  // Log the error message

                // Display the error message in the form
                document.getElementById("error-message").innerText = error.message;
            }
        
        
    }
)