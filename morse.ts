
const morseMap: { [key: string]: string } = {
    A: ".-", B: "-...", C: "-.-.", D: "-..", E: ".", É: "..-..",
    F: "..-.", G: "--.", H: "....", I: "..", J: ".---", 
    K: "-.-", L: ".-..", M: "--", N: "-.", O: "---",
    P: ".--.", Q: "--.-", R: ".-.", S: "...", T: "-", 
    U: "..-", V: "...-", W: ".--", X: "-..-", Y: "-.--", Z: "--..", 
    0: "-----", 1: ".----", 2: "..---", 3: "...--", 4: "....-", 
    5: ".....", 6: "-....", 7: "--...", 8: "---..", 9: "----.",
    ".": ".-.-.-", ",": "--..--", ":": "---...", "?": "..--..", "'": ".----.", "-": "-....-", 
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "\"": ".-..-.",
    "=": "-...-", "UNDERSTOOD": "...-..-", "ERROR": "...-..-.",
    "+": ".-.-.", "INV":"-.-", "WAIT": ".--.-", "END": ".-.-.", "START": "-.-.-",
    "*": "...-..-", "@": ".--.-."
};

const textMap: { [key: string]: string } = Object.fromEntries(
    Object.entries(morseMap).map(([key, value]) => [value, key])
);

function textToMorse(text: string): string {
    return text.toUpperCase().split("").map(char => morseMap[char] || "").join(" ");
}

function morseToText(morse: string): string {
    return morse.trim().split(" ").map(code => textMap[code] || "").join("");
}

async function playMorse(morse: string): Promise<void> {
    for (const symbol of morse) {
        if (symbol === ".") {
            process.stdout.write(".");
            process.stdout.write("\x07")
        } else if (symbol === "-") {
            process.stdout.write("-");
            process.stdout.write("\x07")
            await new Promise(resolve => setTimeout(resolve, 600)); // Longer pause for dash
        } else {
            process.stdout.write(" ");
            await new Promise(resolve => setTimeout(resolve, 300));
        }
    }
    console.log();
}

const input = process.argv[2];
if (!input) {
    console.log("Usage: ts-node morse.ts <text or morse>");
    process.exit(1);
}

if (/^[\.\-\s]+$/.test(input)) {
    const decoded = morseToText(input);
    console.log(decoded);
} else {
    const morse = textToMorse(input);
    console.log(morse);
    playMorse(morse);
}