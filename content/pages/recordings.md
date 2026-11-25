Title: Recordings
Date: 2022-06-10 10:50
Slug: recordings
page-order: 3

Video timestamps are available <input type="button" onClick="document.getElementById('middle').scrollIntoView({behavior: 'smooth'});" value="here">

### Class concert Maastricht Conservatorium
<div id="bLm6PhChfT0" class="embedded-youtube-video"></div>

### Recording session at *Grand Manège* in Namur
<div id="Dnd5uRFL_T0" class="embedded-youtube-video"></div>

### Recording session in private studio in Namur
<div id="eHt73ZqJK2M" class="embedded-youtube-video"></div>

<div id="middle"><h2>Timestamps and programme</h2></div>
<p><a href="javascript:void(0);" onclick="setEmbeddedYouTubeVideoTime('bLm6PhChfT0', 0);">0:00</a> - <b>Jacques Ibert</b>: Concerto for flute and orchestra; 1st movement: Allegro </p>
<p><a href="javascript:void(0);" onclick="setEmbeddedYouTubeVideoTime('bLm6PhChfT0', 305);">5:05</a> - <b>Jacques Ibert</b>: Concerto for flute and orchestra; 2nd movement: Andante </p>
<p><a href="javascript:void(0);" onclick="setEmbeddedYouTubeVideoTime('Dnd5uRFL_T0', 0);">0:00</a> - <b>Franz Schubert</b>: Variations for flute and piano</p>
<p><a href="javascript:void(0);" onclick="setEmbeddedYouTubeVideoTime('eHt73ZqJK2M', 0);">0:00</a> - <b>Toru Takemitsu</b>: Itinérant</p>


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