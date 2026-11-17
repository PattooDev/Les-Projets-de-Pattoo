# Feuille de route

- [x] Identifier la Maker originale sous Linux (USB CDC ACM `20d3:0015`).
- [x] Vérifier l'accès utilisateur au port série.
- [x] Examiner les interfaces du pilote FreeKnife et du transport Inkcut.
- [x] Mettre en place un simulateur hors ligne sans accès USB.
- [ ] Rassembler des captures et spécifications **publiques** du protocole exact Maker ; vérifier leur source et leur licence.
- [ ] Écrire des tests unitaires de cadrage et d'analyse de paquets fictifs.
- [ ] Définir l'intégration sous forme d'extension Inkcut indépendante.
- [ ] Déterminer les prérequis de connexion réels, sans publier de clés.
- [ ] Concevoir validations de trajectoires, limite de force, gestion des erreurs, arrêt d'urgence et procédures de récupération.
- [ ] Envisager un premier essai réel seulement après revue de sécurité et accord explicite du propriétaire.

## À ne pas faire
Ne pas flasher le firmware, ne pas essayer les opcodes de FreeKnife au hasard, ne pas envoyer de G-code directement à la Maker. Les tests hors ligne ne constituent pas une preuve de compatibilité matérielle.
