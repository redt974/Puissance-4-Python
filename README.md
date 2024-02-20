# Puissance 4 en Python avec Tkinter

Ce projet est une implémentation du jeu Puissance 4 en Python avec une interface graphique réalisée avec la bibliothèque Tkinter.

## Installation

1. Assurez-vous d'avoir Python installé sur votre système. Ce code a été testé avec Python 3.7+.
2. Clonez ce dépôt Git sur votre machine :


git clone https://github.com/votre_utilisateur/puissance4-tkinter.git


3. Accédez au répertoire du projet :


cd puissance4-tkinter


4. Exécutez le programme :


python Puissance4.py


## Comment jouer

- Lorsque le jeu démarre, une fenêtre s'ouvre affichant une grille de Puissance 4 vide.
- Les joueurs alternent pour placer leurs pièces dans la grille en cliquant sur la colonne où ils souhaitent placer leur pièce.
- Les pièces tombent vers le bas de la grille et s'empilent les unes sur les autres.
- Le premier joueur à aligner 4 de ses pièces horizontalement, verticalement ou en diagonale gagne la partie.
- Une boîte de dialogue s'affiche pour indiquer quel joueur a gagné la partie.

## Fonctionnalités du code

- La classe `Puissance4` gère la logique du jeu.
- La grille de jeu est représentée par une matrice numpy.
- La bibliothèque Tkinter est utilisée pour créer la fenêtre et les éléments graphiques.
- Les pièces sont affichées sous forme de cercles de couleur rouge et jaune.
- La méthode `winning_move` vérifie s'il y a un alignement gagnant dans la grille.
- L'interface graphique réagit aux clics de souris des joueurs pour placer les pièces sur la grille.

## Auteur

Ce projet a été développé par [Votre Nom](https://github.com/votre_utilisateur).

N'hésitez pas à ouvrir une [issue](https://github.com/votre_utilisateur/puissance4-tkinter/issues) si vous rencontrez des problèmes ou si vous avez des suggestions d'amélioration.
