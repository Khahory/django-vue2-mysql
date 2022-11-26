<template>
    <div>
        <h2 class="subtitle">Anime List</h2>
        
        <!--lista de los animes-->
        <div v-for="anime in animes" class="column is-5">
            <AnimeCard :anime="anime"/>
        </div>
    </div>
</template>

<script>
import AnimeCard from "@/components/AnimeCard";
import {getAPI} from "../../axios-api";

export default {
    name: "AnimeList",
    components: {
        AnimeCard
    },
    data() {
        return {
            animes: []
        }
    },
    created() {
        getAPI.get("/anime/animes/")
            .then(response => {
                this.animes = response.data;
            })
            .catch(error => {
                console.log(error);
            });
    }
}
</script>