<template>
    <div class="row m-1">
        <p class="description-title text-left">
            Распознавание именованных сущностей
        </p>
        <p class="text-left">
            <br>
            Проект для развития компьютерной обработки якутского языка.
            <br>
            <br>
            NER (Named Entity Recognition) - компонент для распознавания именованных сущностей. Задача заключается в
            классификации токенов текста по известным категориям - тэгам: имена людей, локации, организации.
            <br>
            <br>
            Сущности: <span class="card redtext">ORG</span> <span class="card yellowtext">LOC</span> <span
                class="card greentext">PER</span>
        </p>
    </div>
</template>

<script>
    export default {
        name: "Description"
    }
</script>

<style scoped>
    .description-title{
        font-weight: 500;
        font-size: 2rem;
        margin-top: 20px;
        margin-bottom: 0;
        color: black;
    }

    .redtext {
        color: white;
        background-color: rgb(220, 53, 69);
    }

    .yellowtext {
        color: white;
        background-color: rgb(255, 193, 7);
    }

    .greentext {
        color: white;
        background-color: rgb(40, 167, 69);
    }

    .card {
        padding: .4em .4em;
        font-size: 75%;
        line-height: 1;
        text-align: center;
        white-space: nowrap;
        vertical-align: baseline;
        border-radius: .25rem;
        color: white;
        position: relative;
        display: inline-block;
    }

    .card:hover > .tooltip {
        opacity: 1;
    }
</style>