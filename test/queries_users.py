'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: User query list
'''
query_user={      
    'getUser':{ "NEED_TOKEN":True,
        "QUERY":"""
            query GetUser ($page: Int, $limit: Int) {
                getUser(page: $page, limit: $limit) {
                    message
                    status                    
                    error
                    next
                    previous
                    count
                    user_info {
                        id
                        email
                        userFullName
                        username
                        userIdentification
                        userProfessionalCard
                        userPhone
                        userPermissions
                        userLicenses
                        userOrders
                        userOwner
                        hash
                        createdAt
                        modificated
                    }
                }
            }
            """
        },
    'getPosts_userid':{ "NEED_TOKEN":True,
    "QUERY":"""query GetPostByUserId($page: Int, $limit: Int, $userid: Int) {
        getPosts_userid(page: $page, limit: $limit, userid: $userid) {
            data {
            id
            username
            is_vip
            
            posts {
                id
                is_vip
                is_subscriber
                is_paid
                contents{
                gloov_coins
                stickers {
                    id
                    price
                    url
                }
                datatext
                datavideo{url}
                dataimage{url}
                }
                
                user {
                username
                }
                userto
            }
            
            }
            next
            previous
            count
            countall
            status
            message
            error
        }
        }
        """
    },
    'getUserData':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetUserData($user_id: Int) {
        getUserData(user_id: $user_id) {
            status
            message
            error
            data {
            subscription_price
            username
            gender
            birthday_date
            mail
            phone
            country_code
            biography
            created
            first_name
            id
            image_profile
            is_public
            last_name
            link
            modified
            price
            user
            description
            location
            follower
            followings
            follow
            gloovs
            
            is_vip
            is_subscriber
                is_my_profile
            }
        }
        }"""},
    'getProfileContent':{ "NEED_TOKEN":True, 
                        "QUERY": """query getProfileContent(
        $user_id: Int  $content: String
        $page: Int $limit: Int
        ) {
        getProfileContent(
            page: $page limit: $limit
            content: $content user_id: $user_id
        ) {
            data {
            id
            like
            url
            description
            is_vip
            type
            }
            next previous count
            status message error
        }
        }
    """
    },
    'comments':{ "NEED_TOKEN":True, 
                        "QUERY": """query comments($page:Int, $limit:Int, $postId:String) {  
        comments (page:$page, limit:$limit, postId:$postId) {        
        data {      
        created content price
        source types coins  likes
        user{
            id  username avatar
        }
        }
        next, previous, count
        status, message, error
    }  
    }	
    """
    },
    'getFollowings':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetFollowings {
        getFollowings {
            status
            message
            errors
            data {
            id
            image_profile
            is_public
            username
            is_vip
            }
        }
        }
        """
    },
    'getFollowers':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetFollowers($token: String) {
        getFollowers(token: $token) {
            status
            message
            errors
            data {
            id
            image_profile
            is_public
            username
            }
        }
        }
        """
    },
    'get_vault':{ "NEED_TOKEN":True, 
                        "QUERY": """query get_vault($page: Int, $limit: Int, $type_file: String) {
            get_vault(page: $page, limit: $limit, type_file: $type_file) {
                data {
                id
                date
                duration
                height
                idtype
                name
                type
                type_file
                url
                user
                width
                mirror
                }
                next
                previous
                count
                status
                message
                error
            }
            }
        """
    },
    'get_Archived':{ "NEED_TOKEN":True, 
                        "QUERY": """query Get_Archived($page: Int, $limit: Int, $content: String) {
        get_Archived(page: $page, limit: $limit, content:$content) {
            data {
            id
            like
            url
                type
            is_vip
            }
            next
            previous
            count
            status
            message
            error
        }
        }
        """
                        },
    'getStoryProfile':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetStoryProfile($page:Int, $limit:Int, $vip:Boolean) {  
        getStoryProfile(page:$page, limit:$limit, vip:$vip) {        
        data {      
        id 
        destacada
        created      
        vip
        urlvideo
        urlimage
        mirror
        duration
        user{
            username id
        }
        namegroup
        }
        next, previous, count
        status, message, error
    }  
    }"""
                        },
    'get_audiosDefault':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetStoryGroupsAll($page: Int, $limit: Int, $user_id: Int) {
        getStoryGroupsAll(page: $page, limit: $limit, user_id:$user_id) {
            data {
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
            status
            message
            error
            previous
            next
            count
        }
        }"""
                        },
    'getStoryGroup':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetStoryGroup( $id:String) {  
        getStoryGroup(id:$id) {        
        data {   
        name
        vip
        id
        created
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
        status, message, error
        count
    }  
    }	
    """
                        },
    'get_history':{ "NEED_TOKEN":True, 
                        "QUERY": """query get_history($page:Int, $limit:Int) {  
            get_history(page:$page, limit:$limit) {        
            data {      
            id 
            destacada
            created      
            vip
            urlvideo
            urlimage
            mirror
            duration
            user{
                username  id
            }
            }
            next, previous, count
            status, message, error
        }  
        }	
        """
                        },
    'get_audiosDefault':{ "NEED_TOKEN":True, 
                        "QUERY": """query  {   get_audiosDefault  { data {nombre,url } status, error }   }   """
                        },
    'getNotifications':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetNotifications($page: Int, $limit: Int) {
        getNotifications(page: $page, limit: $limit) {
            data {
            avatar
            content_id
            created
            id
            message
            seen
            type_action
            }
            next
            previous    
            status
            message
            errors
        }
        }"""
    },
    'getNotificationsAmount':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetNotificationsAmount {
                getNotificationsAmount {
                    data { notification }
                    status message errors
                }
            }"""
        },
    'getSearch':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetSearch($page:Int, $limit:Int,$character:String) {  
            getSearch(page:$page, limit:$limit,character:$character) {        
            data {      
            id      
            username
            image_profile
            }    
            status, message, errors
            next, previous
        }  
        }	"""
        },
    'getSearchPost':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetSearchPost($page:Int, $limit:Int,$phrase:String) {  
                getSearchPost(page:$page, limit:$limit,phrase:$phrase) {        
                data {      
                id
                type
                url
                description
                }    
                status, message, error
                next,previous, count,countall
            }  
            }	"""
        },
    'getSearchHashtag':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetSearchHashtag($limit:Int,$phrase:String) {  
                getSearchHashtag(limit:$limit,phrase:$phrase) {        
                data {  
                group
                posts{
                    id                
                    description
                    url
                    type
                }
                }    
                status, message, errors
            }  
            }	"""
        },
    'getSearchHashtagGroup':{ "NEED_TOKEN":True, 
                        "QUERY": """query getSearchHashtagGroup($page:Int, $limit:Int, $group:String) {  
            getSearchHashtagGroup(page:$page, limit:$limit,group:$group) {        
            data {        
                id
                type
                url      
                description     
            }
            group
            status, message, errors
            next, previous, count, countall
        }  
        }	"""
        },
    'getSearchPrice':{ "NEED_TOKEN":True, 
                        "QUERY": """query GetSearchPrice($page: Int, $limit: Int, $character: String) {
            getSearchPrice(page: $page, limit: $limit, character: $character) {
                data {
                id first_name last_name
                username image_profile is_vip
                price {
                    subscription private_room
                    messages histories gloovpics
                    gloovideos  gloovtext gloovaudio
                    audio_call video_call
                }
                }
                status  message errors
                next  previous  count  countall
            }
            }"""
        },
    'getCalls':{ "NEED_TOKEN":True, 
                        "QUERY": """qquery getCalls($page: Int, $limit: Int) {
        getCalls(page: $page, limit: $limit) {
            data {
            call{
                call_id
                createdat
                type_call
                time_init
                by_calling
                _id        
            }
            participants
            }
            status  message errors
            next  previous  count  countall
        }
        }"""
        },
    'getInfoProfile':{ "NEED_TOKEN":True, 
                        "QUERY": """query getInfoProfile($user_id: Int) {
        getInfoProfile(user_id: $user_id) {
            data {
            id
            image_profile
            is_paid
            username
            }
            status
            message
            errors
        }
        }"""
        }
}
