# État technique — 17 novembre 2026

## Observations vérifiées
- Identifiant USB de la Maker originale : VID `20d3`, PID `0015`.
- Pilote Linux `cdc_acm` ; port `/dev/ttyACM0` dans cette session.
- Interfaces USB : CDC Communications (0), CDC Data (1) ; endpoints 0x81 notifications IN, 0x02 bulk OUT, 0x82 bulk IN.
- Accès lecture/écriture au nœud autorisé au groupe dialout.
- Aucun test d'envoi de commandes à la machine.

## FreeKnife : analyse du code existant
Le module `src/main/UnofficialCricutDevice/index.js` contient les opcodes `E5` (pré-handshake), `CF` (graine), `0A` (effacement d'erreur), `C7` (négociation AES), `60` (statut), `43` (déplacement), `21` / `22` (début/fin découpe). Il emploie AES-256-ECB pour certains messages et attend des réponses de la machine.

Cette lecture **ne prouve pas** que ces opcodes fonctionnent sur une Maker. Le projet prévoit des configurations de longueurs de paquets variables et requiert des clés externes. Aucune clé n'est intégrée à ce dépôt.

## Inkcut : infrastructure
`DeviceProtocol` expose `init()`, `move()`, `write()`, `data_received()`, `finish()`. Le transport `serialport` fournit la communication asynchrone et relaie les données reçues au protocole. La création d'un adaptateur Maker indépendant semble possible, **sous réserve** de comprendre le protocole propriétaire.

## Incertitudes critiques
1. Cadrage des messages et séquence d'initialisation propres à la Maker.
2. Gestion des clés et du chiffrement, sans publication de secrets.
3. Unités, positionnement, limites mécaniques, pression et vitesse des outils.
4. Acquittements, sécurité et interruption d'urgence.
5. Conditions de redistribution des codes tiers.

Ne pas déduire des paramètres de communication de la seule valeur de `stty`. Aucun pilote fonctionnel n'est revendiqué.
