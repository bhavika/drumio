<%inherit file="layout.mako"/>
<div class="content">
  <p class="lead">Welcome to <span class="font-normal">Drumio</span><br><span class="font-normal">an AI based source separation engine</span>.</p>

  <form ction="/store_track" method="post" accept_charset="utf-8" enctype="multipart/form-data>
    <div class="form-group">
      <label for="mp3">Upload a track</label> <br/>
      <input type="file" class="form-control-file" id="mp3"> <br/>
      <button type="submit" class="btn btn-primary mb-2">Upload</button>
    </div>
  </form>
</div>
