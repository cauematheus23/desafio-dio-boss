const readline = require('readline-sync');

function rank(xp) {
    if (xp <= 1000) {
        return 'Ferro';
    } else if (xp > 1000 && xp <= 2000) {
        return 'Bronze';
    } else if (xp > 2000 && xp <= 5000) {
        return 'Prata';
    } else if (xp > 5000 && xp <= 7000) {
        return 'Ouro';
    } else if (xp > 7000 && xp <= 8000) {
        return 'Platina';
    } else if (xp > 8000 && xp <= 9000) {
        return 'Ascendente';
    } else if (xp > 9000 && xp <= 10000) {
        return 'Imortal';
    } else if (xp > 10000) {
        return 'Radiante';
    }
}

function printInfo(nome, xp) {
    console.log(`O Herói de nome ${nome} está no nível de ${rank(xp)}`);
}

while (true) {
    let nome = readline.question("Qual o nome do personagem? ");
    let xp = parseInt(readline.question(`Quantos de xp tem o ${nome}: `), 10);

    printInfo(nome, xp);

    let resp = readline.question("Quer adicionar outro personagem? [S/N] ").trim();
    if (resp[0].toLowerCase() !== 'n') {
        continue;
    } else {
        break;
    }
}