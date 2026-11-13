Title: Recordings
Date: 2022-06-10 10:50
Slug: recordings
page-order: 3


### Class concert Maastricht Conservatorium
<div id="lvuyUd7FlS4" class="embedded-youtube-video"></div>
<br />
<p><a href="javascript:void(0);" onclick="setEmbeddedYouTubeVideoTime('lvuyUd7FlS4', 240);">4:00</a> - A content
    section in the second video</p>


<script>
    // This code loads the YouTube Iframe Player API code asynchronously.
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/iframe_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    // Get list of embedded YouTube video iframes on the page
    var videoIframes = document.querySelectorAll(".embedded-youtube-video");

    // Once the YouTube API is ready, for each videoIframeId in your array, create
    // a new YT player. Store them in a map object.
    var videoIframeMap = new Map();
    function onYouTubeIframeAPIReady() {
        videoIframes.forEach(function (videoIframe) {
            var videoIframeId = videoIframe.id;
            var player = new YT.Player(videoIframeId, {
                videoId: videoIframeId,
                width: "889px",
                height: "500px",
                events: {
                    'onStateChange': onPlayerStateChange
                },
            });
            videoIframeMap.set(videoIframeId, player);
        });
    }

    // If a video is newly being played, pause all the other videos that are playing.
    // Applies to both them playing via clicking on an embedded video, or via them
    // clicking on a timestamp hyperlink.
    function onPlayerStateChange(event) {
        if(event.data == YT.PlayerState.PLAYING) {
            var newlyPlayingPlayer = event.target;
            // Value in map is a YT Player object, key is the videoId
            videoIframeMap.forEach(function(player, videoId, map) {
                var playerState = player.getPlayerState();
                var isPlaying = playerState == YT.PlayerState.PLAYING || playerState == YT.PlayerState.BUFFERING;
                if((player != newlyPlayingPlayer) && isPlaying) {
                    player.pauseVideo();
                }
            });
        }
    }

    
    function jumpToCurrentlyPlayingVideo() {
        videoIframeMap.forEach(function(player, videoId, map) {
            var playerState = player.getPlayerState();
            var isPlaying = playerState == YT.PlayerState.PLAYING || playerState == YT.PlayerState.BUFFERING;
            if(isPlaying) {
                document.getElementById(videoId).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    }


    // Set the video time for the iframe specified.
    // Look up the player object in the map from before.
    function setEmbeddedYouTubeVideoTime(iframeId, timeInSeconds) {
        var player = videoIframeMap.get(iframeId);
        player.seekTo(timeInSeconds, true);
        player.playVideo();
    }
</script>