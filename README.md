<!-- PROFIL GITHUB DE RESSANE MESSIOUGHI -->
<!-- Banniere et en-tetes : SVG generes maison (assets/) — reseau de noeuds, palette navy / ambre / ciel -->

<p align="center">
  <img src="assets/banner.svg" alt="Ressane Messioughi — Développeur Web Full Stack" width="100%" />
</p>

<p align="center">
  <a href="https://readme-typing-svg.demolab.com">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=F0B429&center=true&vCenter=true&width=720&lines=Développeur+Web+Full+Stack;React+%C2%B7+Node.js+%C2%B7+Express+%C2%B7+MySQL;Temps+réel+avec+Socket.IO;Reconversion+assumée%2C+code+expliqué+ligne+à+ligne" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="mailto:messioughiressane@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/ressane-messioughi/devproject"><img src="https://img.shields.io/badge/DevProject-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <img src="https://komarev.com/ghpvc/?username=ressane-messioughi&label=Vues%20du%20profil&color=F0B429&style=for-the-badge" />
</p>
<!-- LinkedIn : decommenter et coller l'URL quand le profil est pret
  <a href="URL_LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
-->

<img src="assets/headers/01-profil.svg" alt="01 — Qui je suis" width="100%" />

> 🔁 **Reconversion.** Dix ans en logistique, industrie et pharmaceutique, puis retour à
> ce qui m'occupait déjà à 14 ans : administrer des serveurs, manipuler des bases MySQL,
> bidouiller des CMS en PHP. J'en ai fait mon métier.
>
> 🎓 **Titre professionnel DWWM** — développeur web et web mobile, en cours de validation.
>
> 🎯 **Ce que je cherche :** un premier poste où je code tous les jours, où l'on relit mon
> code et où je peux monter en compétences vite. Front, back, ou les deux.

**Ce que je sais faire aujourd'hui, et que je peux expliquer ligne à ligne :** construire
une interface React, concevoir et écrire une API REST, modéliser une base relationnelle et
en écrire le SQL, sécuriser une authentification, et faire communiquer le tout en temps
réel.

<img src="assets/headers/02-projet.svg" alt="02 — Projet principal" width="100%" />

### 🗂️ [DevProject](https://github.com/ressane-messioughi/devproject) — plateforme collaborative de gestion de projet

> Né d'un constat de formation : pendant les travaux de groupe, tout était éparpillé entre
> Discord, Trello, GitHub et des dossiers partagés. Impossible d'avoir une vision d'ensemble.
> DevProject regroupe l'équipe, les rôles, le journal de bord, le suivi des bugs et les
> liens vers les outils existants — dans un seul espace, mis à jour en direct.

| | |
|---|---|
| **Front-end** | React 19 · Vite · Tailwind CSS 4 · React Router 7 · React Hook Form · Socket.IO client |
| **Back-end** | Node.js · Express 5 · MySQL (SQL écrit à la main) · JWT · bcrypt · express-validator · Socket.IO |
| **Qualité** | Vitest · React Testing Library · ESLint · Prettier · Husky · Git Flow |
| **Volume** | 35 composants · 11 pages · 4 391 lignes · 11 tests · 72 commits · 9 versions taguées |

**Trois choses que j'y ai vraiment construites :**

- 🏗️ **Une API en quatre couches strictes** — `routes/` (aiguillage seul), `controllers/`
  (HTTP ↔ métier), `services/` (logique et orchestration), `models/` (seul point de contact
  avec SQL). 9 fichiers de routes, 11 services, 10 modèles. Créer un projet déclenche trois
  opérations liées — créer le projet, créer l'équipe, y ajouter le créateur comme `OWNER` —
  et c'est le service, et lui seul, qui orchestre cette séquence.

- ⚡ **Du temps réel qui sert à quelque chose** — quand un membre ouvre un projet, les autres
  le voient apparaître instantanément. Deux portées de diffusion différentes, et c'est tout
  l'intérêt : `socket.to(salle)` pour la notification, qui part à tout le monde **sauf** à
  celui qui arrive, sinon il verrait son propre nom s'afficher ; `io.to(salle)` pour la liste
  des présents, qui part à **tout le monde**, lui compris, sinon il serait le seul à ne pas
  la voir se remplir.

- 🚦 **Une gestion des erreurs de bout en bout** — validation `express-validator` centralisée
  par domaine, classe `AppError` uniformisée, middleware d'erreurs global en fin de chaîne, et
  côté interface un helper unique qui lit indifféremment les deux formats de réponse pour
  toujours afficher le bon message. Jamais une erreur silencieuse.

<sub>🔒 Le dépôt back-end est privé pour le moment — je le publie sur demande, ou en entretien.</sub>

<img src="assets/headers/03-methode.svg" alt="03 — Ma façon de travailler" width="100%" />

Je n'ai pas empilé des bibliothèques : chaque choix est un choix, et je sais dire pourquoi.

- 🗄️ **SQL écrit à la main, sans ORM** — choix assumé et pédagogique. Écrire moi-même mes
  jointures multi-tables me permet de comprendre et d'expliquer ce que fait chaque requête.
  Toutes utilisent des **paramètres préparés** : c'est la protection de référence contre
  l'injection SQL, appliquée sans exception.

- 🔐 **La sécurité côté serveur, l'interface comme confort** — c'est mon principe directeur :
  *tout ce qui compte réellement est vérifié côté serveur*. Mots de passe hachés avec bcrypt,
  JWT signé vérifié par un middleware sur chaque route protégée, second middleware
  d'autorisation pour les actions réservées au propriétaire. Le front bloque aussi — mais
  seulement pour éviter un aller-retour inutile, jamais comme barrière.

- 🌳 **Git Flow, réellement appliqué** — une branche par fonctionnalité, fusionnée dans `dev`,
  puis dans `main` uniquement à la livraison, avec un tag de version. 20 branches, 9 versions,
  des commits conventionnels (`feat`, `fix`, `perf`, `test`, `docs`). L'historique se lit.

- ✅ **La qualité automatisée, pas promise** — ESLint et Prettier enchaînés par Husky à chaque
  commit : du code non conforme ne peut pas entrer dans l'historique. Zéro erreur ESLint sur
  les deux dépôts.

- 🧪 **Peu de tests, tous maîtrisés** — 11 tests couvrant six natures différentes : fonction
  pure, hook, affichage, interaction, validation métier, remontée d'erreur serveur. Choix
  assumé : je préfère une poignée de tests que je sais expliquer à une couverture large que
  je ne saurais pas défendre.

- ⚡ **La performance mesurée** — les images du projet pesaient **7,9 Mo**, quatorze fois le
  poids de tout le JavaScript. Conversion en WebP, redimensionnement à la taille réelle
  d'affichage, chargement différé : **210 Ko**. Au passage, un bug de casse dans les imports
  qui aurait cassé le déploiement sous Linux.

- ♿ **L'accessibilité prise au sérieux** — un `alt` sur chacune des 24 images sans exception,
  18 attributs `aria-*`, un titre d'onglet propre sur les 11 pages, un seul `<h1>` par page.

- 🤖 **Les outils d'IA, avec une règle** — je m'en sers tous les jours pour aller vite sur ce
  que je sais déjà faire. Mais je relis tout ce qui entre dans mon code : si je ne sais pas
  expliquer une ligne, elle ne reste pas.

<img src="assets/headers/04-stack.svg" alt="04 — Stack technique" width="100%" />

<p align="center">
  <strong>Langages</strong><br/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/SQL-4479A1?logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white" />
</p>

<p align="center">
  <strong>Front-end</strong><br/>
  <img src="https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Vite-646CFF?logo=vite&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind%20CSS-38B2AC?logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/React%20Router-CA4245?logo=reactrouter&logoColor=white" />
  <img src="https://img.shields.io/badge/React%20Hook%20Form-EC5990?logo=reacthookform&logoColor=white" />
  <img src="https://img.shields.io/badge/Framer%20Motion-0055FF?logo=framer&logoColor=white" />
</p>

<p align="center">
  <strong>Back-end &amp; base de données</strong><br/>
  <img src="https://img.shields.io/badge/Node.js-339933?logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Express-000000?logo=express&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Socket.IO-010101?logo=socketdotio&logoColor=white" />
  <img src="https://img.shields.io/badge/JWT-000000?logo=jsonwebtokens&logoColor=white" />
  <img src="https://img.shields.io/badge/Cloudinary-3448C5?logo=cloudinary&logoColor=white" />
</p>

<p align="center">
  <strong>Qualité &amp; outils</strong><br/>
  <img src="https://img.shields.io/badge/Vitest-6E9F18?logo=vitest&logoColor=white" />
  <img src="https://img.shields.io/badge/Testing%20Library-E33332?logo=testinglibrary&logoColor=white" />
  <img src="https://img.shields.io/badge/ESLint-4B32C3?logo=eslint&logoColor=white" />
  <img src="https://img.shields.io/badge/Prettier-F7B93E?logo=prettier&logoColor=black" />
  <img src="https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/Figma-F24E1E?logo=figma&logoColor=white" />
  <img src="https://img.shields.io/badge/Postman-FF6C37?logo=postman&logoColor=white" />
</p>

<img src="assets/headers/05-stats.svg" alt="05 — DevProject en chiffres" width="100%" />

<p align="center">
  <img src="assets/stats.svg" alt="35 composants, 11 pages, 4 391 lignes, 11 tests, 72 commits, 9 versions taguées" width="100%" />
</p>

<img src="assets/headers/06-contact.svg" alt="06 — Me contacter" width="100%" />

Je termine mon titre DWWM et je cherche un **premier poste de développeur web**, en
alternance de front et de back ou spécialisé sur l'un des deux. Je suis basé à **Lyon**.

Si mon travail vous intéresse, le plus simple est d'ouvrir
[**DevProject**](https://github.com/ressane-messioughi/devproject) : le README explique le
projet, et l'historique Git montre comment je travaille.

<p align="center">
  <a href="mailto:messioughiressane@gmail.com"><img src="https://img.shields.io/badge/Écrivez--moi-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</p>

```js
// Ce que je me répète quand je bloque
while (!jeComprends) {
  jeLisLeCodeLigneAligne();
  jEcrisLeProblemeNoirSurBlanc();  // la moitié du temps, ça suffit
}
```

<p align="center">
  <img src="assets/footer.svg" alt="Depuis Lyon, ouvert aux opportunités" width="100%" />
</p>
