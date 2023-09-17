# Exercice 6 : Devoir maison noté
## prérequis
Name: Markdown Preview Mermaid Support
Id: bierner.markdown-mermaid
Description: Adds Mermaid diagram and flowchart support to VS Code's builtin markdown preview
Version: 1.19.0
Publisher: Matt Bierner
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid
## exercice
1. Représenter le schéma E/A de l'énoncé suivant. Une ville (nom, pays) a des musées (nom, description). Une œuvre (titre, siècle) est exposée dans un musée pendant
une certaine période (début, fin). Une œuvre peut ne pas être exposée. Elle peut aussz être exposée dans différents musées à différentes période. On connait le nom
et le prénom de l'artiste qui a réalisé une œuvre. Il y a un artiste par œuvre, les artistes réalisent de nombreuses œuvres. 
2. Album de musique 
- a. Représenter le schéma E/A de l'énoncé suivant. Un album (code, date), identifié par son code, est composé d'une série de plages. Les plages d'un album sont 
numérotées 1,2, ... ; Elles ont une durée. Un album contient au moins une plage. Chaque plage est l'enregistrement d'une seule œuvre, mais une œuvre peut s'étendre 
sur plusieurs plages (par exemple une symphonie en mouvements). Une œuvre a un identifiant et un titre. Certaines oeuvres ne sont pas enregistrées. On connaît les 
interprètes de l'oeuvre pour une plage donnée. Un interprète a un identifiant et un nom et peut jouer de nombreuses œuvres. Une œuvre peut être jouée par plusieurs 
interprètes. 
- b. On suppose que chaque interprète utilise exactement un instrument (piano, guitare, etc) sur une plage. Où placer l'attribut "instrument" dans le schéma 
précédent ? 
1. > (clé = "**clé**")
```mermaid
flowchart LR
EntityClassCity["Ville"]
EntityClassMuseum["Musée"]
EntityClassArtwork["Oeuvre"]
EntityClassArtist["Artiste"]
AssociationClassIsIn{{"est dans"}}
AssociationClassExhibitedAtTheMuseumDuring{{"exposé au musée pendant"}}
AssociationClassHasMade{{"a réalisé"}}
CityAttribute1(["`**nom**`"])
CityAttribute2(["pays"])
MuseumAttribute1(["`**nom**`"])
MuseumAttribute2(["description"])
ArtworkAttribute1(["`**titre**`"])
ArtworkAttribute2(["siècle"])
ArtistAttribute1(["`**nom**`"])
ArtistAttribute2(["prénom"])
ExhibitedAtTheMuseumDuringAttribute1(["début"])
ExhibitedAtTheMuseumDuringAttribute2(["fin"])
ExhibitedAtTheMuseumDuringAttribute3(["`**id**`"])
EntityClassCity --- CityAttribute1
EntityClassCity --- CityAttribute2
EntityClassMuseum --- MuseumAttribute1
EntityClassMuseum --- MuseumAttribute2
EntityClassArtwork --- ArtworkAttribute1
EntityClassArtwork --- ArtworkAttribute2
EntityClassArtist --- ArtistAttribute1
EntityClassArtist --- ArtistAttribute2
AssociationClassExhibitedAtTheMuseumDuring --- ExhibitedAtTheMuseumDuringAttribute1
AssociationClassExhibitedAtTheMuseumDuring --- ExhibitedAtTheMuseumDuringAttribute2
AssociationClassExhibitedAtTheMuseumDuring --- ExhibitedAtTheMuseumDuringAttribute3
EntityClassArtist -- 1:n --> AssociationClassHasMade
AssociationClassHasMade -- 1:1 --> EntityClassArtwork
EntityClassArtwork -- 0:1 --> AssociationClassExhibitedAtTheMuseumDuring
AssociationClassExhibitedAtTheMuseumDuring -- 1:n --> EntityClassMuseum
EntityClassMuseum -- 1:1 --> AssociationClassIsIn
AssociationClassIsIn -- 1:n --> EntityClassCity
```
2. EntityClass
- a.
```mermaid
flowchart LR
EntityClassAmbum["album"]
EntityClassTrack["plage"]
EntityClassArtwork["oeuvre"]
EntityClassInterpreter["interprète"]
AssociationClassIsPartOf{{"fait partie de"}}
AssociationClassIsDividedInto{{"est divisé en"}}
AssociationClassHasMade{{"a fait"}}
AssociationClassUse{{"utilise"}}
AlbumAttribute1(["`**code**`"])
AlbumAttribute2(["date"])
TrackAttribute1(["`**numéro**`"])
TrackAttribute2(["durée"])
ArtworkAttribute1(["`**identifiant**`"])
ArtworkAttribute2(["titre"])
InterpreterAttribute1(["`**identifiant**`"])
InterpreterAttribute2(["nom"])
UseAttribute(["instrument"])
EntityClassInterpreter -- 1:n --> AssociationClassHasMade
AssociationClassHasMade -- 1:n --> EntityClassArtwork
EntityClassArtwork -- 1:n --> AssociationClassIsDividedInto
AssociationClassIsDividedInto -- 1:n --> EntityClassTrack
EntityClassTrack -- 1:1 --> AssociationClassIsPartOf
AssociationClassIsPartOf -- 1:n --> EntityClassAmbum
EntityClassInterpreter -- 1:n --> AssociationClassUse
AssociationClassUse -- 1:n --> EntityClassTrack
EntityClassInterpreter --- InterpreterAttribute1
EntityClassInterpreter --- InterpreterAttribute2
EntityClassArtwork --- ArtworkAttribute1
EntityClassArtwork --- ArtworkAttribute2
EntityClassTrack --- TrackAttribute1
EntityClassTrack --- TrackAttribute2
EntityClassAmbum --- AlbumAttribute1
EntityClassAmbum --- AlbumAttribute2
AssociationClassUse --- UseAttribute
```