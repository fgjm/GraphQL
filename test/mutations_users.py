'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: User mutation list
'''
mutation_user={      
    'createPostUserTo':{ "NEED_TOKEN":True,
        "QUERY":"""mutation createPostUserTo(
            $description: String $location: String $text: String
            $userto: String $is_vip: Boolean $price: Int
            ) {
            createPostUserTo(
                r: {
                description: $description location: $location text: $text
                userto: $userto is_vip: $is_vip price: $price
                }
            ) {
                data {
                id
                userto
                description
                location
                is_vip
                price
                contents { datatext }
                }
                message status error
            }
            }
            """
        },
    'createPost':{ "NEED_TOKEN":True,
    "QUERY":"""mutation createPost(
        $description: String $location: String $text: String
        $is_vip: Boolean $price: Int
        ) {
        createPost(
            r: {
            description: $description location: $location
            text: $text is_vip: $is_vip price: $price
            }
        ) {
            data {
            id
            userto
            is_vip
            price
            description
            location
            contents {
                datatext
            }
            }
            message
            status
        }
        }
        """
    },
    'updatePost':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation updatePost(
            $postId: String
            $description: String
            $location: String
            $text: String
            $userto: String
            ) {
            updatePost(
                r: {
                description: $description
                location: $location
                text: $text
                userto: $userto
                }
                postId: $postId
            ) {
                data {
                id
                userto
                description
                location
                contents {
                    datatext
                }
                }
                message
                status
            }
            }
            """
            },
    'deletePost':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation deletePost($postId: String) {
        deletePost(postId: $postId) {
            data {
            id
            }
            message
            status
        }
        }
    """
    },
    'posts_birthday':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation posts_birthday(
        $user_to: Int
        $type_content: String
        $sticker_id: Int
        $coins: Int
        ) {
        posts_birthday(
            user_to: $user_to
            type_content: $type_content
            sticker_id: $sticker_id
            coins: $coins
        ) {
            data {
            id
            userto
            contents {
                gloov_coins
                stickers {
                id
                price
                url
                }
            }
            }
            message
            status
        }
        }
    """
    },
    'comments':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation  comments($text:String, $type:String, $postId:String){
        comments( r: {    
            text: $text,
            types: $type
        }, postId:$postId) 
        {
            data{   
            comments{   
                created
                coins           
                price
                source
                types
                content
                likes 
                    user{
                id
                username
                avatar
            }  
            }      
            }
            message   
            status
            error
        }
        }
        """
    },
    'like':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation like($postId:String){
        like(postId:$postId) {
            status, message
            data{like, id}
        }
        }
        """
    },
    'archived':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation Archived{
        archived(postId:"647103f16c98bffeb9dd8f4d") {
            status, message
            data{
                archived}
        }
        }
        """
    },
    'followCreate':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation FollowCreate($userId:Int, $token:String) {
        followCreate(userId:$userId, token:$token) {
            error
            message
            status
            data {
            follow
            acepted
            }
        }
        }
        """
                        },
    'seenNotification':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation SeenNotification($id_notification: Int) {
        seenNotification(id_notification: $id_notification) {
            errors
            message
            status
            data {
            seen
            }
        }
        }"""
                        },
    'storyGroup':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation storyGroup($list: [String], $name:String, $vip:Boolean){
        storyGroup(list: $list, name:$name, vip:$vip) {
            status
            message
            error
            data{
                name
            created
            modificated
            vip
            id
            story {
                id
                destacada
                created
                vip
                urlvideo
                urlimage
                mirror
                duration
                user {
                username
                id
                }
            }    
            }
        }
        }"""
                        },
    'editStoryGroup':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation EditStoryGroup($list: [String], $name:String, $id:String){
        editStoryGroup(list: $list, name:$name, id:$id) {
            status
            message
            error
            data{
                name
            created
            modificated
            vip
            id
            story {
                id
                destacada
                created
                vip
                urlvideo
                urlimage
                mirror
                duration
                user {
                username
                id
                }
            }    
            }
        }
        }	
    """
                        },
    'deleteStoryGroup':{ "NEED_TOKEN":True, 
                        "QUERY": """mutation deleteStoryGroup( $id:String){
        deleteStoryGroup( id:$id) {
            status
            message
            error
        }
        }"""
        }
}
