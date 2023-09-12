Exercice 5 : 
On considère une course nautique qui se déroule en plusieurs épreuves sanctionnées chacune par un classement des bateaux participants, chaque bateau participant à,
l'épreuve même s'il n'arrive pas au bout de l'épreuve (dernière position). Il y a une seule épreuve par jour, chaque épreuve débute et se termine dans un port, le
port pouvant être différent du port de départ. Chaque bateau a un numéro d'immatriculation, un nom et une longueur. Il a un skipper et un équipage et est financé par
un ou plusieurs sponsors. Le skipper d'un bateau ne peut pas changer d'une épreuve à l'autre de la course, en revanche la composition des équipiers d'un bateau peut
changer d'une épreuve à l'autre de la course. La base de données doit permettre de répondre, entre autres, aux questions suivantes :
- Quels sont les sponsors d'un bateau ?
- Quel est le montant de la subvention d'un sponsor particulier à un bateau particulier ?
- Quels bateaux sont engagés dans l'épreuve qui débute le 27 Avril ?
- Quels sont les équipiers du bateau qui a gagné la première épreuve ?
- Sur quels bateaux de plus de 12 mètres un équipier médecin est-il engagé ?
1. Proposez un schéma E/ A qui modélise la course nautique.
2. Dans votre schéma E/ A, est-ce qu 'un équipier peut être engagé sur plusieurs bateaux pendant la même épreuve ? Si oui, modifier le schéma E/ A afin de préciser
qu'un équipier ne peut pas être sur plusieurs bateaux pendant une épreuve.

`(les clés interne sont en gras et les clés externe en italique)`
```mermaid
flowchart LR
EntityClassBoat["Bateau"]
EntityClassSponsor["Sponsor"]
EntityClassTest["Épreuve"]
EntityClassSeaport["Port"]
AssociationClassFinance{{"finance"}}
AssociationClassParticipate{{"participe"}}
AssociationClassTakesPlace{{"se déroule"}}
BoatAttribute1(["`**immatriculation**`"])
BoatAttribute2(["longueur"])
BoatAttribute3(["skipper"])
BoatAttribute4(["nom"])
SponsorAttribute1(["`**nom**`"])
TestAttribute1(["`**date**`"])
TestAttribute2(["classement"])
TestAttribute3(["durée"])
SeaportAttribute1(["`**nom**`"])
FinanceAttribute1(["`**somme**`"])
ParticipateAttribute1(["`**équipe**`"])
ParticipateAttribute2(["y a-t-il un médecin ?"])
EntityClassSponsor -- 1:n --- AssociationClassFinance
AssociationClassFinance -- 1:n --- EntityClassBoat
EntityClassBoat -- 1:n --> AssociationClassParticipate
AssociationClassParticipate -- 2:n --> EntityClassTest
EntityClassTest -- 1:n --> AssociationClassTakesPlace
AssociationClassTakesPlace -- 1:n --> EntityClassSeaport
EntityClassBoat --- BoatAttribute1
EntityClassBoat --- BoatAttribute2
EntityClassBoat --- BoatAttribute3
EntityClassBoat --- BoatAttribute4
EntityClassSponsor --- SponsorAttribute1
EntityClassTest --- TestAttribute1
EntityClassTest --- TestAttribute2
EntityClassTest --- TestAttribute3
EntityClassSeaport --- SeaportAttribute1
AssociationClassFinance --- FinanceAttribute1
AssociationClassParticipate --- ParticipateAttribute1
AssociationClassParticipate --- ParticipateAttribute2
```