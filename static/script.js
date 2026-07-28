window.onload = function () {

    const result = document.body.dataset.result;

    console.log("Result =", result);

    if (result === "win") {
        document.getElementById("winSound").play().catch(console.error);
    }
    else if (result === "lose") {
        document.getElementById("loseSound").play().catch(console.error);
    }
    else if (result === "draw") {
        document.getElementById("drawSound").play().catch(console.error);
    }

};