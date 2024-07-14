# Port Scan

Ce script Python permet de scanner les ports ouverts sur une adresse IP spécifiée, en utilisant des threads pour un scan rapide et efficace. Il utilise la bibliothèque socket pour établir des connexions et détecter les ports ouverts. De plus, il affiche le type de service associé à chaque port ouvert (HTTP, HTTPS, FTP, etc.), ce qui aide à identifier rapidement les services disponibles sur la machine cible.

## Fonctionnalités
Scan rapide des ports : Utilisation de threads pour scanner les ports de manière parallèle, accélérant ainsi le processus de détection.

### Détection du type de service : 
Utilisation de socket.getservbyport(port) pour identifier le service associé à chaque port ouvert (si disponible).

### Interface utilisateur agréable : 
Art ASCII coloré en violet et menu interactif pour une expérience utilisateur améliorée.

### Compatible multi-plateforme : 
Fonctionne sur les systèmes d'exploitation Windows, Linux et macOS grâce à l'utilisation de os.system pour effacer la console (cls pour Windows et clear pour les autres systèmes).

## Utilisation

1. Clonez le repository ou téléchargez le script.

2. Assurez-vous d'avoir Python installé sur votre machine.

3. Exécutez le script en spécifiant l'adresse IP à scanner.

## Exemple d'utilisation:

Copier le code

```python ip.py```


## Remarques
Ce script est conçu pour une utilisation éducative et de démonstration. Assurez-vous d'avoir l'autorisation légale appropriée avant de scanner des adresses IP ou des réseaux qui ne vous appartiennent pas.
