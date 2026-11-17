# Cricut découpe — Deepin 25 / Linux

**Statut : expérimental. Aucun pilote de découpe opérationnel n'est encore disponible dans ce projet.**

Objectif : explorer un moyen libre de préparer et, à terme, envoyer des découpes SVG à une Cricut Maker originale, avec son firmware d'origine, en réutilisant les logiciels et recherches existants.

## Matériel vérifié (17 novembre 2026)
- Cricut Maker première génération : USB `20d3:0015` (Provo Craft & Novelty Inc).
- Interfaces USB CDC ACM, pilote Linux `cdc_acm`, port observé `/dev/ttyACM0`.
- Lecture/écriture du port autorisées via le groupe `dialout`.
- Aucun échange applicatif ni mouvement testé. Les droits d'accès ne prouvent pas la compatibilité du protocole.
- Une vitesse `9600 baud` affichée par stty ne suffit pas à déterminer les paramètres de communication de la machine.

## Travaux existants
- [Inkcut](https://github.com/inkcut/inkcut) : SVG, trajectoires, filtres et transport série bidirectionnel.
- [FreeKnife](https://github.com/OddPig/FreeKnife) : rétro-ingénierie expérimentale du protocole Cricut, principalement sur Explore Air 2. **Ne pas l'essayer directement sur la Maker.**
- [Discussion Inkcut #426](https://github.com/inkcut/inkcut/issues/426) : proposition d'intégration d'un pilote Cricut.
- [Étude Maker sous Linux](https://bradleygannon.com/blog/2026/cricut-maker-not-quite-on-linux/) : observations sur les échanges USB.
- [CutCutGo](https://github.com/virtualabs/cutcutgo) : firmware de remplacement nécessitant des opérations matérielles, écarté pour la phase initiale.

Il n'est pas établi que le firmware Cricut accepte G-code ou HPGL. Le protocole, son initialisation et son chiffrement restent à valider pour `20d3:0015`.

## Structure
- `simulation/` : simulateur Python **hors ligne**, sans connexion série.
- `docs/ETAT_TECHNIQUE.md` : éléments connus, inconnues et précautions.
- `docs/FEUILLE_DE_ROUTE.md` : développement par étapes.
- `docs/FACEBOOK.md` : présentation publique.

## Démonstration sans matériel
```bash
python3 cricut-decoupe/simulation/simulateur.py
```
Le simulateur crée uniquement des données JSON dans la console. Il n'ouvre aucun périphérique USB.

## Règle de sécurité
Pas de changement de firmware, pas d'envoi de données ni de mouvement sur la Maker avant validation du protocole, gestion des erreurs et consentement du propriétaire. Ne jamais publier des numéros de série ou des clés privées.

Ce dépôt ne revendique aucun code tiers : réutilisation future soumise à vérification des licences. Projet indépendant, sans affiliation avec Cricut.
