async function sendRequest() {

    const url = document.getElementById("url").value;
    const method = document.getElementById("method").value;

    let payload = {};

    try {
        const text = document.getElementById("payload").value;

        if (text) {
            payload = JSON.parse(text);
        }
    }
    catch {
        alert("Invalid JSON payload");
        return;
    }

    const response = await fetch("/api/test", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            url: url,
            method: method,
            payload: payload
        })
    });

    const result = await response.json();

    document.getElementById("result").innerHTML =
        `<pre>${JSON.stringify(result, null, 2)}</pre>`;
}