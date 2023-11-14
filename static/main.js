
const {createApp} = Vue

const Taskapp = {
    data(){
        return{
            task:'Your will became programmer not now but soon',
            tasks:[
                {task_name:'study'},
                {task_name:'learn'},
                {task_name:'code'}
            ]
        }
    },
    delimiters:['{','}']
}

createApp(Taskapp).mount('#app')
