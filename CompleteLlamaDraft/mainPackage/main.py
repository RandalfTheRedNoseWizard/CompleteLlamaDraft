import dataPackage
from locationPackage.decryptedLocation import findLocation
from moviePackage.decryptedMovie import decrypt_movie_title

def main():
    # Paths to files
    json_file = 'dataPackage/EncryptedGroupHints Fall 2024 Section 001.json'
    english_file = 'dataPackage/UCEnglish.txt'
    encrypted_message = "gAAAAABnJ6xXVDc2AOy9IsNcfodS3viOIxRb_yskmNX2rLff-yUIeTxS-Hgv4H2tRTikS0xj0QUmIcc12aJZSxmtoPcXxabAaRKiSLWLcV6ATkPecfeag22bi4dLejPjXBitOOkeN9Rt5OIiT96z8kuxg9Z6CSFMQw=="
    movie_key = "oSQSToOvQLs-_7SRDonuB1xB7K10RwCF7MdlQa1MCdc="

    # Decrypt the location
    location_finder = findLocation(json_file, english_file)
    project_team_name = "CompleteLlama"
    location = location_finder.decrypt_location(project_team_name)
    print(f"Decrypted UC Location: {location}")

    # Decrypt the movie title
    movie_title = decrypt_movie_title(encrypted_message, movie_key)
    print(f"Decrypted Movie Title: {movie_title}")

if __name__ == "__main__":
    main()
