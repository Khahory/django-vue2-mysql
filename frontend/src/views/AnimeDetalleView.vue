<template>
    <div>
        <h1 class="title">{{ $route.params.titulo }}</h1>
        <img :src="'http://192.168.0.5:8000'+$route.params.image" alt="anime-img-alt">
    </div>
</template>

<script>
export default {
    name: "AnimeDetalleView"
}
</script>

<style scoped>

</style>