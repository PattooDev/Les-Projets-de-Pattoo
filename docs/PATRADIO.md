# PatRadio — Centre d’écoute radio mondial

**Auteur : Patrick "Pattoo" Ventresque (PattooDev)**

**Statut : v0.2 testée sur Deepin 25** · Python / PyQt6 · interface en français.

## À quoi sert PatRadio ?

PatRadio réunit dans une application Linux indépendante des liens vers des récepteurs radio accessibles sur Internet. On peut ainsi explorer les communications de radioamateurs, les échanges entre pilotes et contrôleurs aériens, certains flux maritimes et des radios internationales depuis Firefox, **sans acheter de récepteur ni installer d’antenne chez soi**.

## Fonctionnalités vérifiées

- Interface graphique PyQt6 lancée sous Deepin 25.
- Catégories d’écoute et fréquences préconfigurées.
- Ouverture des récepteurs dans Firefox.
- Sur le WebSDR de Twente, ouverture automatique sur **7 120 kHz / LSB**.
- Audio fonctionnel après activation dans le navigateur.
- Favoris sauvegardés et retrouvés après redémarrage de PatRadio.
- Lanceur sur le bureau Deepin.
- Aucune modification de PatDesk.

## Ce que PatRadio ne fait pas

PatRadio n’est pas un récepteur SDR local et ne décode pas lui-même les transmissions. La réception, les langues, les fréquences disponibles et les flux audio dépendent des services tiers. Une fréquence préréglée n’assure pas qu’une communication soit active. Certains flux peuvent être indisponibles ou soumis aux conditions de leurs fournisseurs.

## Installation et code source

La version expérimentée a été installée sur Deepin 25 avec Python et PyQt6. Le code complet de l’application doit encore être publié dans un dépôt PatRadio dédié ; **ce document est une présentation du projet et non le dépôt du logiciel**.

## Attribution et licence prévue

Projet de Patrick "Pattoo" Ventresque (PattooDev). Pour une publication future du code source, licence GPLv3 ou ultérieure envisagée, avec conservation d’une attribution appropriée à l’auteur et au projet dans les conditions permises par la licence.
