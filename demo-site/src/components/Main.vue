<template>
    <div class="row justify-content-start m-1">
        <b-form-textarea
                class="col-12"
                id="textarea"
                v-model="text"
                placeholder="Enter something..."
                rows="3"
                max-rows="6"
        ></b-form-textarea>
        <div class="m-0 col-lg-12 row p-0 justify-content-start">
            <b-button class="mt-4" id="button" variant="primary" @click="getNerTags">Спросить</b-button>
        </div>
        <Results v-bind:results="results"></Results>
    </div>
</template>

<script>
    import Results from "./Results";

    export default {
        name: "Main",
        components: {Results},
        data() {
            return {
                text: '',
                results: []
            }
        },
        methods: {
            getNerTags() {
                if (this.$data.text == '') {
                    alert('Заполните все поля!')
                    return
                }
                this.axios.post('http://sakhaner.ru:8000/', {
                    text: this.$data.text
                }).then((response) => {
                    this.$data.results.push(response.data)
                }).catch((e) => {
                    console.log(e)
                    alert('Ошибка сети! Попробуйте еще раз.')
                })
            }
        }
    }
</script>

<style scoped>

</style>