<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="page_d_acceuil.css" />
        <link rel="stylesheet" href="header.css">
        <link rel="stylesheet" href="form.css">
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script type="text/javascript" src="follow_share_and_action_for_post.js"></script>
        <title>Blog</title>
    </head>
    <body>
        <header>
            <nav>
                <ul id="topBar">
                    <li id="acceuil">
                        <a href="./page_d_acceuil_connected.php">
                            <svg version="1.1" id="homeIcon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                            viewBox="0 0 460.298 460.297" xml:space="preserve" >
                                <path d="M230.149,120.939L65.986,256.274c0,0.191-0.048,0.472-0.144,0.855c-0.094,0.38-0.144,0.656-0.144,0.852v137.041
                                c0,4.948,1.809,9.236,5.426,12.847c3.616,3.613,7.898,5.431,12.847,5.431h109.63V303.664h73.097v109.64h109.629
                                c4.948,0,9.236-1.814,12.847-5.435c3.617-3.607,5.432-7.898,5.432-12.847V257.981c0-0.76-0.104-1.334-0.288-1.707L230.149,120.939
                                z"/>

                                <path d="M457.122,225.438L394.6,173.476V56.989c0-2.663-0.856-4.853-2.574-6.567c-1.704-1.712-3.894-2.568-6.563-2.568h-54.816
                                c-2.666,0-4.855,0.856-6.57,2.568c-1.711,1.714-2.566,3.905-2.566,6.567v55.673l-69.662-58.245
                                c-6.084-4.949-13.318-7.423-21.694-7.423c-8.375,0-15.608,2.474-21.698,7.423L3.172,225.438c-1.903,1.52-2.946,3.566-3.14,6.136
                                c-0.193,2.568,0.472,4.811,1.997,6.713l17.701,21.128c1.525,1.712,3.521,2.759,5.996,3.142c2.285,0.192,4.57-0.476,6.855-1.998
                                L230.149,95.817l197.57,164.741c1.526,1.328,3.521,1.991,5.996,1.991h0.858c2.471-0.376,4.463-1.43,5.996-3.138l17.703-21.125
                                c1.522-1.906,2.189-4.145,1.991-6.716C460.068,229.007,459.021,226.961,457.122,225.438z"/>
                            </svg>
                        </a>
                        <a href="#mostRecentPost">Post les plus récents</a>
                        <a href="#postFromFollowed">Post de vos abonnements</a>
                        <a href="#postRankedByNumberOfShare">Post les plus partagés</a>
                        <a href="./posts/createAPost.php">Créer un post</a>
                    </li>
                    <li>
                        <form id="searchBar" action="./search_answer.php" method="get">
                            <div>
                                <label for="keyword">recherche :</label>
                                <input type="text" id="keyword" name="keyword">
                            </div>
                            <div>
                                <button type="submit" >
                                    <svg focusable="false" viewBox="0 0 24 24">
                                        <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
                                    </svg>
                                </button>
                            </div>
                        </form>
                    </li>
                    <li id="username">
                        username
                        <img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username">
                    </li>
                </ul>
            </nav>
        </header>
        <section id="pageContent">
            <section id="mostPopularUsers">
                <nav class="users">
                    <ul>
                        <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                        <li>username</li>
                        <li>
                            <button class="followButton username" id="popularUser" onclick="follow(this)">
                                <span>Follow</span>
                                <img src="./assets/signeValidation.png" height="20" width="20">
                            </button>
                        </li>
                    </ul>
                    <p>number of folowers</p>
                </nav>
            </section>
            <section id="forPost">
                <section id="mostRecentPost">
                    <h1>Les 2 derniers posts les plus récents :</h1>
                    <article id="usernamedatetime">
                        <header>
                            <ul>
                                <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                <li>username</li>
                                <li class="liFollow">                            
                                    <button class="followButton username" id="popularUser" onclick="follow(this)">
                                        <span>Follow</span>
                                        <img src="./assets/signeValidation.png" height="20" width="20">
                                    </button>
                                </li>
                                <li class="datetime">datetime</li>
                            </ul>
                        </header>
                        <section class="postContent">
                            <img src="./assets/wallpaper.png" alt="imagePost" />
                            <br />
                            <p>blabla ;)</p>
                        </section>
                        <footer>
                            <section class="postFooter">
                                <ul>
                                    <li class="partage">
                                        <button class="shareButton username" onclick="share(this)">
                                        </button>
                                        <p>nombre de partage</p>
                                    </li>
                                    <li>
                                        <button class="commentButton username" onclick="ouvrirCommentaire(this)">
                                            <svg viewBox="0 0 48 48" width="22" height="19">
                                                <path d="M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z"></path>
                                            </svg>
                                        </button>
                                        nombre de commentaires
                                    </li>
                                    <li>
                                        <button onclick="ouvrirModif(this)">
                                            <svg fill="#000000" width="22" height="19" viewBox="-2.5 -2.5 24 24" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin">
                                                <path d="M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z"/>
                                            </svg>
                                        </button>
                                    </li>
                                    <li>
                                        <button onclick="supprimerPost(this)">
                                            <svg fill="#000000" width="22" height="19" viewBox="0 0 36 36" version="1.1"  preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                <path class="clr-i-solid clr-i-solid-path-1" d="M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z"></path>
                                                <path class="clr-i-solid clr-i-solid-path-2" d="M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z"></path>
                                                <rect x="0" y="0" width="36" height="36" fill-opacity="0"/>
                                            </svg>
                                        </button>
                                    </li>
                                </ul>
                            </section>
                            <section class="comment">
                                <article id="usernamedatetime1">
                                    <header>
                                        <ul>
                                            <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                            <li>username</li>
                                            <li class="liFollow">                            
                                                <button class="followButton username" id="popularUser" onclick="follow(this)">
                                                    <span>Follow</span>
                                                    <img src="./assets/signeValidation.png" height="20" width="20">
                                                </button>
                                            </li>
                                            <li class="datetime">datetime</li>
                                        </ul>
                                    </header>
                                    <section class="postContent">
                                        <p>blabla ;)</p>
                                    </section>
                                    <footer>
                                        <section class="postFooter">
                                            <ul>
                                                <li class="partage">
                                                    <button class="shareButton username" onclick="share(this)">
                                                    </button>
                                                    <p>nombre de partage</p>
                                                </li>
                                            </ul>
                                        </section>
                                    </footer>
                                </article>
                                <article id="usernamedatetime2">
                                    <header>
                                        <ul>
                                            <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                            <li>username</li>
                                            <li class="liFollow">                            
                                                <button class="followButton username" id="popularUser" onclick="follow(this)">
                                                    <span>Follow</span>
                                                    <img src="./assets/signeValidation.png" height="20" width="20">
                                                </button>
                                            </li>
                                            <li class="datetime">datetime</li>
                                        </ul>
                                    </header>
                                    <section class="postContent">
                                        <img src="./assets/wallpaper.png" alt="imagePost" />
                                        <br />
                                        <p>blabla ;)</p>
                                    </section>
                                    <footer>
                                        <section class="postFooter">
                                            <ul>
                                                <li class="partage">
                                                    <button class="shareButton username" onclick="share(this)">
                                                    </button>
                                                    <p>nombre de partage</p>
                                                </li>
                                                <li>
                                                    <button onclick="ouvrirModif(this)">
                                                        <svg class="editButton" fill="#000000" width="22" height="19" viewBox="-2.5 -2.5 24 24" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin">
                                                            <path d="M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z"/>
                                                        </svg>
                                                    </button>
                                                </li>
                                                <li>
                                                    <button onclick="supprimerPost(this)">
                                                        <svg class="deleteButton" fill="#000000" width="22" height="19" viewBox="0 0 36 36" version="1.1"  preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                            <path class="clr-i-solid clr-i-solid-path-1" d="M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z"></path>
                                                            <path class="clr-i-solid clr-i-solid-path-2" d="M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z"></path>
                                                            <rect x="0" y="0" width="36" height="36" fill-opacity="0"/>
                                                        </svg>
                                                    </button>
                                                </li>
                                            </ul>
                                        </section>
                                        <article class="modification">
                                            <header>
                                                <form class="modifForm">
                                                    <label for="postText">Texte Post:</label>
                                                    <textarea class="texteModification" name="texteModification" rows="5" cols="40"></textarea>
                                                    <br /> <label for="image">Image :</label>
                                                    <input class="imageModification" type="file" name="image">
                                                    <br>
                                                </form>
                                            
                                                <button class="submitModifForm" onclick="soumettreModification(this)"><span>submit the form!</span></button>
                                            </header>
                                    </footer>
                                </article>
                                <article class="commentFormSection">
                                    <header>
                                        <form class="commentForm">
                                            Commentaire:
                                            <textarea class="texteCommentaire" name="texteCommentaire" rows="5" cols="40"></textarea>
                                            <br /> <label for="image">Image :</label>
                                            <input class="imageCommentaire" type="file" name="image">
                                            <br>
                                        </form>
                                    
                                        <button class="submitCommentForm" onclick="soumettreCommentaire(this)"><span>submit the form!</span></button>
                                    </header>
                                    <footer>
                                        <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                        <h1 class="commentPreview">
                                            SENT: <span></span>
                                            <img src="#" alt="rien" />
                                        </h1>

                                        <div class="consoleCommentaire"></div>
                                    </footer>
                                </article>
                            </section>
                            <article class="modification">
                                <header>
                                    <form class="modifForm">
                                        <label for="postText">Texte Post:</label>
                                        <textarea class="texteModification" name="texteModification" rows="5" cols="40"></textarea>
                                        <br /> <label for="image">Image :</label>
                                        <input class="imageModification" type="file" name="image">
                                        <br>
                                    </form>
                                
                                    <button class="submitModifForm" onclick="soumettreModification(this)"><span>submit the form!</span></button>
                                </header>
                                <footer>
                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                    <h1 class="modifPreview">
                                        SENT: <span></span>
                                        <img src="#" alt="rien" />
                                    </h1>

                                    <div class="consoleModification"></div>
                                </footer>
                            </article>
                        </footer>
                    </article>
                </section>
                <section id="postFromFollowed">
                    <h1>Les posts de vos abonnement :</h1>
                    <article id="usernamedatetime3">
                        <header>
                            <ul>
                                <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                <li>username</li>
                                <li class="liFollow">                            
                                    <button class="followButton username" id="popularUser" onclick="follow(this)">
                                        <span>Follow</span>
                                        <img src="./assets/signeValidation.png" height="20" width="20">
                                    </button>
                                </li>
                                <li class="datetime">datetime</li>
                            </ul>
                        </header>
                        <section class="postContent">
                            <p>blabla ;)</p>
                        </section>
                        <footer>
                            <section class="postFooter">
                                <ul>
                                    <li class="partage">
                                        <button class="shareButton username" onclick="share(this)">
                                        </button>
                                        <p>nombre de partage</p>
                                    </li>
                                    <li class="commentaires">
                                        <button class="commentButton username" onclick="ouvrirCommentaire(this)">
                                            <svg viewBox="0 0 48 48" width="22" height="19">
                                                <path d="M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z"></path>
                                            </svg>
                                        </button>
                                        nombre de commentaires
                                    </li>
                                </ul>
                            </section>
                            <section class="comment">
                                <article id="usernamedatetime4">
                                    <header>
                                        <ul>
                                            <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                            <li>username</li>
                                            <li class="liFollow">                            
                                                <button class="followButton username" id="popularUser" onclick="follow(this)">
                                                    <span>Follow</span>
                                                    <img src="./assets/signeValidation.png" height="20" width="20">
                                                </button>
                                            </li>
                                            <li class="datetime">datetime</li>
                                        </ul>
                                    </header>
                                    <section class="postContent">
                                        <p>blabla ;)</p>
                                    </section>
                                    <footer>
                                        <section class="postFooter">
                                            <ul>
                                                <li class="partage">
                                                    <button class="shareButton username" onclick="share(this)">
                                                    </button>
                                                    <p>nombre de partage</p>
                                                </li>
                                            </ul>
                                        </section>
                                    </footer>
                                </article>
                                <article id="usernamedatetime5">
                                    <header>
                                        <ul>
                                            <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                            <li>username</li>
                                            <li class="liFollow">                            
                                                <button class="followButton username" id="popularUser" onclick="follow(this)">
                                                    <span>Follow</span>
                                                    <img src="./assets/signeValidation.png" height="20" width="20">
                                                </button>
                                            </li>
                                            <li class="datetime">datetime</li>
                                        </ul>
                                    </header>
                                    <section class="postContent">
                                        <p>blabla ;)</p>
                                    </section>
                                    <footer>
                                        <section class="postFooter">
                                            <ul>
                                                <li class="partage">
                                                    <button class="shareButton username" onclick="share(this)">
                                                    </button>
                                                    <p>nombre de partage</p>
                                                </li>
                                            </ul>
                                        </section>
                                    </footer>
                                </article>
                                <article class="commentFormSection">
                                    <header>
                                        <form class="commentForm">
                                            Commentaire:
                                            <textarea class="texteCommentaire" name="texteCommentaire" rows="5" cols="40"></textarea>
                                            <br /> <label for="image">Image :</label>
                                            <input class="imageCommentaire" type="file" name="image">
                                            <br>
                                        </form>
                                    
                                        <button class="submitCommentForm" onclick="soumettreCommentaire(this)"><span>submit the form!</span></button>
                                    </header>
                                    <footer>
                                        <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                        <h1 class="commentPreview">
                                            SENT: <span></span>
                                            <img src="#" alt="rien" />
                                        </h1>

                                        <div class="consoleCommentaire"></div>
                                    </footer>
                                </article>
                            </section>
                        </footer>
                    </article>
                </section>
                <section id="postRankedByNumberOfShare">
                    <h1>Les posts les plus partagés :</h1>
                    <article id="usernamedatetime3">
                        <header>
                            <ul>
                                <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                <li>username</li>
                                <li class="liFollow">                            
                                    <button class="followButton username" id="popularUser" onclick="follow(this)">
                                        <span>Follow</span>
                                        <img src="./assets/signeValidation.png" height="20" width="20">
                                    </button>
                                </li>
                                <li class="datetime">datetime</li>
                            </ul>
                        </header>
                        <section class="postContent">
                            <p>blabla ;)</p>
                        </section>
                        <footer>
                            <section class="postFooter">
                                <ul>
                                    <li class="partage">
                                        <button class="shareButton username" onclick="share(this)">
                                        </button>
                                        <p>nombre de partage</p>
                                    </li>
                                    <li class="commentaires">
                                        <button class="commentButton username" onclick="ouvrirCommentaire(this)">
                                            <svg viewBox="0 0 48 48" width="22" height="19">
                                                <path d="M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z"></path>
                                            </svg>
                                        </button>
                                        nombre de commentaires
                                    </li>
                                </ul>
                            </section>
                            <section class="comment">
                                <article id="usernamedatetime4">
                                    <header>
                                        <ul>
                                            <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                            <li>username</li>
                                            <li class="liFollow">                            
                                                <button class="followButton username" id="popularUser" onclick="follow(this)">
                                                    <span>Follow</span>
                                                    <img src="./assets/signeValidation.png" height="20" width="20">
                                                </button>
                                            </li>
                                            <li class="datetime">datetime</li>
                                        </ul>
                                    </header>
                                    <section class="postContent">
                                        <p>blabla ;)</p>
                                    </section>
                                    <footer>
                                        <section class="postFooter">
                                            <ul>
                                                <li class="partage">
                                                    <button class="shareButton username" onclick="share(this)">
                                                    </button>
                                                    <p>nombre de partage</p>
                                                </li>
                                            </ul>
                                        </section>
                                    </footer>
                                </article>
                                <article id="usernamedatetime5">
                                    <header>
                                        <ul>
                                            <li><img src="./accounts/pfp/default_pfp.png" alt="photo de profil de username" width="30" height="30"></li>
                                            <li>username</li>
                                            <li class="liFollow">                            
                                                <button class="followButton username" id="popularUser" onclick="follow(this)">
                                                    <span>Follow</span>
                                                    <img src="./assets/signeValidation.png" height="20" width="20">
                                                </button>
                                            </li>
                                            <li class="datetime">datetime</li>
                                        </ul>
                                    </header>
                                    <section class="postContent">
                                        <p>blabla ;)</p>
                                    </section>
                                    <footer>
                                        <section class="postFooter">
                                            <ul>
                                                <li class="partage">
                                                    <button class="shareButton username" onclick="share(this)">
                                                    </button>
                                                    <p>nombre de partage</p>
                                                </li>
                                            </ul>
                                        </section>
                                    </footer>
                                </article>
                                <article class="commentFormSection">
                                    <header>
                                        <form class="commentForm">
                                            Commentaire:
                                            <textarea class="texteCommentaire" name="texteCommentaire" rows="5" cols="40"></textarea>
                                            <br /> <label for="image">Image :</label>
                                            <input class="imageCommentaire" type="file" name="image">
                                            <br>
                                        </form>
                                    
                                        <button class="submitCommentForm" onclick="soumettreCommentaire(this)"><span>submit the form!</span></button>
                                    </header>
                                    <footer>
                                        <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                        <h1 class="commentPreview">
                                            SENT: <span></span>
                                            <img src="#" alt="rien" />
                                        </h1>

                                        <div class="consoleCommentaire"></div>
                                    </footer>
                                </article>
                            </section>
                        </footer>
                    </article>
                </section>
            </section>
        </section>
    </body>
</html>