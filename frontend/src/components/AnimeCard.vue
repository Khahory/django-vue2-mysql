<template>
    <section>
        <b-collapse
            class="card"
            animation="slide"
            aria-id="contentIdForA11y3">
            <template #trigger="props">
                <div
                    class="card-header"
                    role="button"
                    aria-controls="contentIdForA11y3"
                    :aria-expanded="props.open">
                    <p class="card-header-title">
                        {{ anime.titulo }} &nbsp;
                        <a>#{{ anime.estado }}</a>.
                    </p>
                    <a class="card-header-icon">
                        <b-icon
                            :icon="props.open ? 'menu-down' : 'menu-up'">
                        </b-icon>
                    </a>
                </div>
            </template>
            
            <div class="card-content">
                <div class="content">
                    {{ anime.descripcion }}
                    <p class="mt-4">Fecha de concluido: <b>{{ anime.concluido }}</b></p>
                </div>
            </div>
            <footer class="card-footer">
                <router-link :to="{name: 'anime', params: {
                        id: anime.id,
                        titulo: anime.titulo,
                        image: anime.image,
                        slug: anime.slug
                    }}">
                    <a class="card-footer-item">Detalles</a>
                </router-link>
            </footer>
        </b-collapse>
    </section>
</template>

<script>
export default {
    name: "AnimeCard",
    props: {
        anime: {
            type: Object,
            required: true
        }
    }
}
</script>
